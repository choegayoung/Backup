import json
import os

FILE_PATH = "./data/storage.json"

def empty():
  print("함수 정의가 되어 있지 않습니다.")

def getData():
  if not os.path.exists(FILE_PATH):
    result = { "t2_storage": [] }
  else :
    f = open(FILE_PATH, "r", encoding="utf-8")
    result = json.load(f)
    f.close()
  return result

def setData(data):
  if not os.path.exists(FILE_PATH):
    pass
  else :  
    f = open(FILE_PATH, "w", encoding="utf-8")
    json.dump(data, f, ensure_ascii=False)
    f.close()
  list(None)

# 시작

def add(args):
	data = getData()
	id = max( (word["id"] for word in data["t2_storage"]), default = 0) + 1
	row = { "id" : id , "word" : args.content }
	data["t2_storage"].append(row)
	setData(data)

def update(args):
	data= getData()
	for i in range(len(data["t2_storage"])):
		if data['t2_storage'][i]['id'] == int(args.id):
			data['t2_storage'][i]['word'] = args.content
			break
	setData(data)

def remove(args):
	data=getData()
	for i in range(len(data["t2_storage"])):
		if data["t2_storage"][i]["id"] == int(args.id):
			del data["t2_storage"][i]
			break
	setData(data)

def list(args):
	data = getData()
	if len(data["t2_storage"])>0:
		row1 = "="*50
		row2 = "-" *50
		print(row1)
		print(f'ID \t 단어')
		for i in range(len(data["t2_storage"])):
			print(row2)
			print(f'{data["t2_storage"][i]["id"]}\t{data["t2_storage"][i]["word"]}')
	else : print("데이터가 없습니다.")