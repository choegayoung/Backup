from fastapi import FastAPI ,Form # << form 으로 데이터를 받으려면 Form 을 import 해와야함
from fastapi.responses import HTMLResponse

app = FastAPI()

arr = [] # << 서버가 종료될 때 까지 이용가능, 종료 후 재시작하면 초기화


@app.get("/") 
def root(txt: str =""): 
   return {"status" : True, "txt" : txt}

@app.post("/{var}") # << 경로변수 (다른 함수에서 지정한 패스가 자동으로 변수에 담긴다.)
def root(id: str = Form(""), # << http body 를 받을 수 있는 메소드(post, put, delete) 에서 이용.
         pwd: str =  Form(""),
         var: str = ""
         ):
   arr.append({"id": id, "pwd": pwd}) # << arr에 이 값들을 넣겠다
   print(arr)
   return {"status" : True, "id" : id, "pwd" : pwd, "var" : var} # << 받은 값들을 보여준다.

@app.get("/view", response_class=HTMLResponse)
def view():
   return """
        <body>
            <form action = "/login" method = "post">  
                <input type ="text" name="id" />
                <input type ="password" name="pwd" />
                <button type ="submit">요청</button>
            </form>
        </body>

        </body>
        """