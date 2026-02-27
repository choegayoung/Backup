import json

def getData() : 
    f= open("./data/memo.json", "r", encoding="utf-8")
    return json.load(f)

def add(word) : 
    data = getData()
    result = word
    data ["list"].append(result)
    print (data, result)
    f = open("./data/memo.json", "w", encoding="utf-8")
    json.dump(data, f, ensure_ascii=False)

def list() :
    print("list() 호출")
    data = getData()
    arr = data["list"]
    for v in arr: print(v)

def remove(word) : 
    data = getData()
    result = [v for v in data.list if v != word]
    data["list"].append(result)
    print (data, result)
    f = open("./data/memo.json", "w", encoding="utf-8")
    json.dump(data, f, ensure_ascii=False)