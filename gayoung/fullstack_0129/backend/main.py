from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from db import findOne, save
import uuid
from settings import settings

SECRET_KEY = "your-extremely-secure-random-secret-key" # 서버만 알 수 있는 비밀키
ALGORITHM = "HS256" # 사용할 암호화 방식
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # 유효시간

def set_token(sub: int, email: str):        # <<토큰을 만드는 함수. 유저의 번호와 email을 인자로 받겠다
    try:
        iat = datetime.now(timezone.utc)    # << 발행 시간 정의. 영국표준시를 기준으로 한국시간을 나타낸다.
        exp = iat + (timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)) # << 토큰 만료 시간 정의. 발행시간으로부터 30분 뒤에 만료된다
        data= {                             # 토큰 안에 넣을 정보들
                "email" : email,            # 유저의 이메일을 받겠다
                "iss":"EDU",                # 발행자 정의
                "sub": str(sub),            # 유저 번호
                "iat": iat,                 # 발행 시간을 위에 정의한 시간으로 지정
                "exp": exp}                 # 만료 시간을 위에 정의한 시간으로 지정
        
        return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM) # << 위 데이터를 우리만의 비밀키와 암호화 방식으로 섞어서 토큰을 발급
    except JWTError as e:
        print(f"JWT Error : {e}")
    return None

class LoginModel(BaseModel):                # << 로그인 모델은 이런 모양이어야해!
    email: str
    pwd: str


app = FastAPI()

app.add_middleware(
       CORSMiddleware,
    allow_origins="http://localhost:5173",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return{"status": True}

@app.post("/login")             
def login(model: LoginModel):
    sql=f"select * from team2.user where `email` = '{model.email}' and `password` = '{model.pwd}'"      # << 입력받은 값이랑 DB테이블에 있는 정보가 같은지?
    data = findOne(sql)
    if data:
        access_token = set_token(data["no"],data["email"])  # << 만약 정보가 맞으면 토큰을 발급할거야. 만들려면 유저 번호랑 이메일이 필요하니까 그걸로 만들게
    return {"status": True, "access_token": access_token}   # << 상태값 정답, 토큰은 만들어진 토큰.

@app.post("/token")
def token():
    result = set_token(2)
    return{result}

@app.post("/key")               # << 프론트에서 /key 라고 요청하면 실행할 함수
def key(model:LoginModel):
    sql = f"""
    select * from team2.user 
    where `email` = '{model.email}' and `password` = '{model.pwd}'
    """
    data = findOne(sql)         # << 로그인 한 계정의 열을 모두 가져온다
    if data :
        id = uuid.uuid4().hex
        token = set_token(str(data["no"]),data["email"])
        sql = f"""
        INSERT INTO team2.`login` (`id`, `userNo`, `token`) VALUE ('{id}',{data["no"]},'{token}') 
        """
        if save(sql) :
            return { "status": True, "access_token": id}
    return {"status": False }
