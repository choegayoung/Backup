import json

def add(a, b):
    print(int (a) + int (b))

def list () :
    print("list() 호출됨")
    f = open("./data/memo.json" , "r" , encoding="utf-8")
    data = json.load(f) ## 자료형을 dict으로 바꿔주는 함수
    arr = data["list"] 
     ## print(data["list"]) 텍스트를 추출할 때에는 [] 사용
    for v in arr : print(v)