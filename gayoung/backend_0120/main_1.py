import mariadb
from dotenv import load_dotenv
load_dotenv()
import os

try:
    conn = mariadb.connect(
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('HOST'),
        port=int(os.getenv('PORT')),
        database=os.getenv('DATABASE')
    )
    print(conn,type(conn))
    cur = conn.cursor()
    sql = "select 10 as no"


except mariadb.Error as e:
    print(f"MariaDB Error : {e}")