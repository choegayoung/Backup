from fastapi import APIRouter
from config.db import getconn
import mariadb

router = APIRouter(prefix="/user" ,tags=["사용자"])

print(getconn())
@router.get(path="")
def user():
    try:
        conn = getconn()  # 내 db연결 정보를 conn에 넣겠다
        cur = conn.cursor() # conn으로 접속해서 쿼리에 작성할 수 있게 하겠다
        sql = "select * from edu.test" # 명령어
        cur.execute(sql) # sql에 쓴걸 쿼리에 요청하겠다

        columns = [desc[0] for desc in cur.description] # 각 컬럼의 정보가 담긴 튜플리스트를 불러오는데 그 중에 첫번째 (컬럼명)를 출력하겠다
        rows = cur.fetchall() # 각 컬럼에 들어있는 value를 모두모두 불러오겠다, 그걸 rows라고 하겠다
        result = [dict(zip(columns,row)) for row in rows] # rows 안에 있는 내용물을 row라고 할거고, 컬럼명과 묶어서 객체로 출력하겠다.
        cur.close() # 쿼리작성을 종료하겠다
        conn.close() # db연결을 종료하겠다
        return {"status": True, "result": result} # 그 결과를 출력하겠다
    except mariadb.Error as e: # mariadb에 에러가 있으면 그걸 e라고 부르겠다
        print(f"sql 오류 : {e}") # 그러면 e를 출력할거다
        return {"status": False}


@router.post(path="")
def user():
    return {"Hello": "World"}

@router.put(path="")
def user():
    return {"Hello": "World"}

@router.delete(path="")
def user():
    return {"Hello": "World"}


