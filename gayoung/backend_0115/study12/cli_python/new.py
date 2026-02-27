def list():
 data=getData()
 line1 = "=" *50
 line2 = "-" *50
 if len(data["words"]) > 0 :
   print(line1)
   print(f'번호\t내용')
   for i in range(len(data["words"])) :
     if i < len(data["words"]) : print(line2)
     print(f'{data["words"][i]["id"]},{data["words"][i]["word"]}')
   print(line1)
 else:
  print("데이터가 없습니다")