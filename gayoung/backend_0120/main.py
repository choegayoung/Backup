import mariadb
from dotenv import load_dotenv
load_dotenv()
import os 

def getConn():
    try:
     return mariadb.connect(
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('HOST'),
        port=int(os.getenv('PORT')),
        database=os.getenv('DATABASE')
        )
    except mariadb.Error as e:
     print(f"MariaDB Error : {e}")
    return None



def findOne(sql):
    result = None
    try:
        conn = getConn()
        if conn:
            cur = conn.cursor()
            cur.execute(sql)
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]

            cur.close()
            conn.close()
            result = dict(zip(columns,row)) if row else None
    except mariadb.Error as e:
        print(f"MariaDB Error : {e}")
    return result
    
   
def findAll(sql):
    result = []
    try:
        conn = getConn()
        if conn:
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
    # cur.fetchall() 전체의 행을 받을 때 쓰는 함수
    # cur.fetchone() 하나의 행을 받을 때 쓰는 함수
            columns = [desc[0] for desc in cur.description]

    # 전체의 행을 출력할 때
    #result = [dict(zip(columns,row)) for row in rows]
    #print(result)

    # 하나의 행을 출력할 때
    #result = dict(zip(columns,row) if row else None)
    #print(result)

            cur.close() # 종료할 때는 역순으로 종료.
            conn.close()
            result = [dict(zip(columns,row)) for row in rows]

    except mariadb.Error as e:
        print(f"MariaDB Error : {e}")
    return result


def save(sql):
    result = False
    try:
        conn = getConn()
        if conn:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
            result = True
    except mariadb.Error as e:
        print(f"MariaDB Error : {e}")
    return result


deptNo1 = "d001"
deptNo2 = "d002"
deptNo3 = "d009"
deptlist = [deptNo1,deptNo2,deptNo3]

sql1 = f"""
       SELECT dept_no, count(emp_no) AS cnt
        FROM edu.dept_emp 
        WHERE dept_no IN {tuple(deptlist)}
        GROUP BY dept_no
        ORDER BY 2 DESC
        """
#print(sql)
#print (findOne(sql))
#print (findAll(sql))

sql2 = "SELECT * FROM edu.test"
print(findAll(sql2))

name = "가영"
sql3 = f"""
        INSERT INTO edu.test 
        (`name`, `regDate`) 

        VALUE ('{name}',NOW())
"""
print(save(sql3))
print(findAll(sql2))