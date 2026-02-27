from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel  # << 스키마를 정의해준다. 데이터형식을 규정할 수 있음
from db import findOne, findAll, save
import mariadb

origins = [
  "http://localhost:5173"     # << 기본적으로 허용할 내 리액트 도메인
]

class LoginModel(BaseModel):  # << LoginModel은 이런 모양이어야해!
  email: str
  pwd: str

app = FastAPI()
app.add_middleware(           # << 리액트에 어느정도까지 권한을 줄건지?
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
  return {"status": True, "result": ["공유는 해드림"]}

@app.post("/login")           # << 서버주소 뒤에 login을 붙여서 데이터를 보내면 이 함수 실행
def login(loginModel: LoginModel, response: Response):  # << loginModel이 뒤에 정의한 모양이어야하고, response는 응답값(fastAPI에서 제공)
  msg = "잘못된 정보 입니다."   
  try:
    sql = f"""
      select * from edu.user 
       WHERE `delYn` = 0 
         AND `email` = '{loginModel.email}' 
         AND `password` = '{loginModel.pwd}'
    """
    data = findOne(sql)     # << DB에서 사용자 정보를 찾겠다
    if data:                # << 있으면
      response.set_cookie(  # << response에 있는 기능 중 쿠키를 만드는 기능을 이용하겠다
        key="user",         # << 쿠키 이름은 user
        value=data["no"],   # << 그 안에는 고유번호를 넣겠다
        max_age=60 * 60,        # 1시간 (초)
        expires=60 * 60,        # max_age와 유사 (초)
        path="/",
        domain="localhost",     # << 쿠키가 유효한 도메인 설정
        secure=True,            # HTTPS에서만 전송 (http는 해당X)
        httponly=True,          # JS 접근 차단 (⭐ 보안 중요)
        samesite="lax",         # 'lax' 중간 | 'strict' 많이 | 'none' 조금 : 보안수준으로 토큰을 다른 곳에서 발급받아 오지 못하도록 설정
      )
      return {"status": True}
  except mariadb.Error as e:
    print(f"SQL 오류 : {e}")
  return {"status": False, "message": msg}

@app.post("/logout")        # << 서버 주소 뒤에 logout을 붙여서 데이터를 보내면 이 함수 실행
def logout(response: Response):       # <<  response에는 응답값이 들어갈건데
  response.delete_cookie(key="user")  # << 근데 로그아웃을 하면 그 응답값에 키가 user라고 있는 쿠키를 지울게
  return {"status": True}

@app.get("/user")
def user(request: Request):
  email = request.cookies.get("user")
  if email:
    return {"status": True, "me": email}
  else:
    return {"status": False}
