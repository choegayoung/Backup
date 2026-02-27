from fastapi import APIRouter
from config.db import getconn
import mariadb

router = APIRouter(tags=["기본"])


@router.get(path="/")
def root():
    try:
        conn = getconn()
        cur = conn.cursor()
        sql = "select 1 as no"
        cur.execute(sql)
        columns = [desc[0] for desc in cur.description]
        row = cur.fetchone()
        result = dict(zip(columns, row)) if row else None
        return {"status": True, "result":result}
    except mariadb.Error as e:
        print(f'sql오류 : {e}')
        return {"status": False}

