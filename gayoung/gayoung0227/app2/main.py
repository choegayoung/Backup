from fastapi import FastAPI, Request, Response, Cookie
from settings import settings
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx
import redis
import uuid


oauth = OAuth()
oauth.register(
    name = 'kakao',
    client_id = settings.client_id,
    client_secret = settings.client_secret,
    authorize_url = "https://kauth.kakao.com/oauth/authorize",
    access_token_url = "https://kauth.kakao.com/oauth/token",
    api_base_url = "https://kapi.kakao.com",
    client_kwargs = {"scope": "profile_nickname profile_image"}

)

# client1 = redis.Redis( host="redis", port=6379, db=0, decode_responses=True)
# client2 = redis.Redis( host="redis", port=6379, db=1, decode_responses=True)
client1 = redis.Redis( host="redis-service", port=6379, db=0, decode_responses=True)
client2 = redis.Redis( host="redis-service", port=6379, db=1, decode_responses=True)

app = FastAPI(title=settings.title, root_path=settings.root_path)
origins = [ "http://localhost","http://localhost:5173", "http://aiedu.tplinkdns.com:6213" ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
  SessionMiddleware,
  secret_key="your-secret-key-here"
)

async def getToken(client, code: str):
  return await client.post(
    "https://kauth.kakao.com/oauth/token",
    data={
      "grant_type": "authorization_code",
      "client_id": settings.client_id,
      # "redirect_uri": "http://localhost:8000/oauth/callback/kakao",
      # "redirect_uri": "http://t2s4.quadecologics.cloud:6203/oauth/callback/kakao",
      "redirect_uri": "http://aiedu.tplinkdns.com:6203/app1/oauth/callback/kakao",
      "code": code,
      "client_secret": settings.client_secret,
    },
    headers={"Content-Type": "application/x-www-form-urlencoded"}
  )

async def getUserInfo(client, access_token: str):
  return await client.get(
    "https://kapi.kakao.com/v2/user/me",
    headers={"Authorization": f"Bearer {access_token}"})

async def setUserLogout(client, access_token: str):
  return await client.post(
    "https://kapi.kakao.com/v1/user/logout",
    headers={"Authorization": f"Bearer {access_token}"})

@app.get("/")
def read_root():
  return {"service": "App2"}

@app.get("/login/kakao")
async def kakaoLogin(request: Request):
  # redirect_uri = "http://localhost:8000/oauth/callback/kakao"
  # redirect_uri = "http://t2s4.quadecologics.cloud:6203/oauth/callback/kakao"
  redirect_uri = "http://aiedu.tplinkdns.com:6203/app1/oauth/callback/kakao"
  return await oauth.kakao.authorize_redirect(request, redirect_uri)

@app.get("/oauth/callback/kakao")
async def kakaoCallback(code: str, response: Response):
  async with httpx.AsyncClient() as client:
    tokenResponse = await getToken(client, code)
    tokens = tokenResponse.json()
    access_token = tokens.get("access_token")
    expires_in = tokens.get("expires_in")

    refresh_token = tokens.get("refresh_token")
    refresh_token_expires_in = tokens.get("refresh_token_expires_in")

    id = uuid.uuid4().hex
    client1.setex(id,int(refresh_token_expires_in),access_token)
    client2.setex(id,int(refresh_token_expires_in),refresh_token)

    response.set_cookie(
      key = "accept",
      value = id,
      max_age = int(expires_in),
      expires = int(expires_in),
      path="/",
      # domain="localhost",
      # domain="t2s4.quadecologics.cloud",
      domain="aiedu.tplinkdns.com",
      secure = False,
      httponly = True,
      samesite="lax"
    )



    # response.set_cookie(
    #   key = "access_token",
    #   value = access_token,
    #   max_age = int(expires_in),
    #   expires = int(expires_in),
    #   path="/",
    #   # domain="localhost",
    #   domain="t2s4.quadecologics.cloud",
    #   secure = False,
    #   httponly = True,
    #   samesite="lax"
    # )




    # response.set_cookie(
    #   key = "refresh_token",
    #   value = refresh_token,
    #   max_age = int(refresh_token_expires_in),
    #   expires = int(refresh_token_expires_in),
    #   path="/",
    #   # domain="localhost",
    #   domain="t2s4.quadecologics.cloud",
    #   secure = False,
    #   httponly = True,
    #   samesite="lax"
    # )
    

    return RedirectResponse(url = "http://aiedu.tplinkdns.com:6213")
    # return {"status": True, "token": access_token}
  return{"status": False}
  # kakao = oauth.create_client('kakao')
  # access_token = await oauth.kakao.authorize_access_token(request)
  # return {"access_token": access_token}

@app.get("/me")
async def me(accept: str = Cookie(default = None)):
  if accept:
    access_token = client1.get(accept)
    print(accept, access_token)
    async with httpx.AsyncClient() as client:
      userResponse = await getUserInfo(client,access_token)
      userInfo = userResponse.json()

      if userResponse.status_code == 200:
        user = {
          "id": userInfo.get("id"),
          "nickname" : userInfo.get("properties")["nickname"],
          "profile_image" : userInfo.get("properties")["profile_image"]
        }
        return {"status": True,"userInfo":user}
  return {"status": False}

@app.get("/logout")
async def logout(request: Request, response: Response, accept: str = Cookie(default = None)):
  if accept:
    access_token = client1.get(accept)
    async with httpx.AsyncClient() as client:
      logoutResponse = await setUserLogout(client, access_token)
      if logoutResponse.status_code == 200:
        client1.delete(accept)
        client2.delete(accept)
        for cookieName in request.cookies.keys():
          response.delete_cookie(
              key=cookieName,
              domain="aiedu.tplinkdns.com"
              # domain="t2s4.quadecologics.cloud"
          )
        return{"status" : True, "msg": "쿠키삭제"}
  return{"status" : False}