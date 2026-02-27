from db import findOne, findAll, save

def empty():  
    print("함수 정의가 되어 있지 않습니다.")
  
def select(args):
    sql = """
          select `id`,
           `word` ,
           `nickname` ,
           date_format(`regDate`,'%y-%m-%d %H:%i:%s') as regDate
          from edu.study
          """
    list = findAll(sql)
    print(f"번호\t글자\t생성일자")
    print("-"*50)
    for row in list:
      print(f"{row["id"]}\t{row["nickname"]}\t{row["word"]}\t{row["regDate"]}")
    pass

def insert(args):
    sql = f"INSERT INTO edu.study (`nickname`,`word`) VALUE ('가영','{args.word}');" 
    save(sql)
    select(None)
    pass

def update(args): 
    sql = f"UPDATE edu.study SET `word` = '{args.word}' WHERE `id` = {args.id};"
    save(sql)
    select(None)
    pass

def delete(args): 
    sql = f"DELETE FROM edu.study WHERE `id` = {args.id} ;"
    save(sql)
    select(None)
    pass

