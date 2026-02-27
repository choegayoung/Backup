import os
import mariadb
from dotenv import load_dotenv
load_dotenv()

def getConn():
  try:
    return mariadb.connect(
      user=os.getenv('DB_USER'),
      password=os.getenv('DB_PASSWORD'),
      host=os.getenv('DB_HOST'),
      port=int(os.getenv('DB_PORT')),
      database=os.getenv('DB_DATABASE')
    )
  except mariadb.Error as e:
    print(f"MariaDB Error : {e}")
    return None
  
def findOne(sql):
  result = None
  conn = getConn()
  try:
    cur = conn.cursor()
    cur.execute(sql)
    row = cur.fetchone() 
    columns = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()
    result = dict(zip(columns, row)) if row else None
  except mariadb.Error as e:
    print(f"MariaDB Error : {e}")
    conn.rollback()
    conn.close()
  return result
  
def findAll(sql):
  result = []
  conn = getConn()
  try:
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall() 
    columns = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()
    result = [dict(zip(columns, row)) for row in rows]
  except mariadb.Error as e:
    print(f"MariaDB Error : {e}")
    conn.rollback()
    conn.close()
  return result

def save(sql):
  result = False
  conn = getConn()
  try:
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    result = True
  except mariadb.Error as e:
    print(f"MariaDB Error : {e}")
    conn.rollback()
    conn.close()
  return result
