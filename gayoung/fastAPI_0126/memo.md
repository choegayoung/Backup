## fastAPI 설치 방법

UV 설치 Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | more"

UV 프로젝트 초기화 프로젝트 폴더 생성 후 실행
uv init .

FastAPI 모듈 추가
uv add fastapi --extra standard

FastAPI 기본 설정 main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
FastAPI 실행 Service Run
uv run fastapi dev

## Http의 메소드 5가지

get : 조회, select
post : 생성, insert
put : 전체수정, update
delete : 삭제, delete
path : 부분수정, 잘안씀


frontend쪽 관련은 fastapi에서 관리하지 않음