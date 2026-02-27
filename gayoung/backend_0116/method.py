import json

FLIE_PATH = "./data/memo.json"

def getData():
  f = open(FLIE_PATH, "r", encoding="utf-8")
  result = json.load(f)
  f.close
  return result

def setData(data):
  f = open(FLIE_PATH, "w", encoding="utf-8")
  json.dump(data, f, ensure_ascii=False)
  f.close
  list()

def 목록(a):
  print("목록 호출 완료")

def 입력(a):
  print("입력: ", a.t)

def 수정(a):
  print("수정: ", a.k, a.t)
  
def 삭제(a):
  print("삭제: ", a.k)