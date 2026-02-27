from fastapi import FastAPI
from fastapi.responses import HTMLResponse # << return에 html 형식으로 쓸 수 있게함

app = FastAPI() # << was(웹 애플리케이션 서버)를 만들기 위함. 필수!, 다른파일도 불가. 무조건 main.py에 있어야함.
                # 포트 변경을 하고싶으면 uv run fastapi dev -- 0000
                # uv run fastapi run 을 하면 0.0.0.0.8000 으로 url생성, 모두가 들어올 수 있게 함
                # 다른 피씨에서 접근할 수 있게 하려면 uv run fastapi run

arr = [] # << 서버가 종료될 때 까지 이용가능, 종료 후 재시작하면 초기화


@app.get("/", response_class=HTMLResponse) # << 진짜 화면으로 표현 
def root(txt: str =""): 
    print(f"전역 배열 : {arr}")
    print(f"전달 받은 변수 : {txt}")
    if txt == "":
        return """
        <body>
            <form>
                <input type="text" name ="txt" />
                <button type = "submit">전송</button>
            </form>
        </body>
    """
    else:
        arr.append(txt)
        html = ""
        for v in arr:
            html += f"<li>{v}</li>"
        return f"""
                <body>
                <ul>{html}</ul>
                <a href ="/">돌아가기</a>
                </body>
            """