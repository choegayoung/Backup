from db import findOne, findAll, save

def empty():
  print("함수 정의가 되어 있지 않습니다.")

def userList(args):
  sql=f'''
      select * from user
      where `delYn` =0
      '''
  print(f'번호\t이름\t이메일\t비밀번호\t성별\t탈퇴여부\t회원등록일자\t회원정보수정일자')
  print('-'*50)
  list=findAll(sql)
  for row in list:
    print(f'{row['no']}\t{row['name']}\t{row['email']}\t{row['password']}\t{row['gender']}\t{row['delYn']}\t{row['regDate']}\t{row['modDate']}')

def boardList(args):
  sql=f'''
      select post.no, post.title, post.content, user.name,post.regDate,post.modDate
      from team2.post
      inner join team2.user
      on (`user`.no=post.user_no)
      where post.delYn=0
      '''
  print(f'번호\t제목\t내용\t글작성자\t글작성일자\t글수정일자')
  print('-'*50)
  list=findAll(sql)
  for row in list:
    print(f'{row['no']}\t{row['title']}\t{row['content']}\t{row['name']}\t{row['regDate']}\t{row['modDate']}')
  

def userAdd(args):
  sql = f'''
        INSERT INTO `user`(`name`, `email`, `password`, `gender`)
        VALUE ('{args.name}','{args.email}','{args.password}','{args.gender}')
        '''
  save(sql)
  userList(None)

def boardAdd(args):
  sql = f'''
        INSERT INTO `post`(`title`, `content`, `user_no`)
        VALUE ('{args.title}','{args.content}','{args.user_no}')
        '''
  save(sql)
  boardList(None)

def userDetail(args):
  sql=f'''
      select * from user
      where `delYn` = 0 and `no` = {args.no}
      '''
  print(f'번호\t이름\t이메일\t비밀번호\t성별\t탈퇴여부\t회원등록일자\t회원정보수정일자')
  print('-'*50)
  list = findAll(sql)
  for row in list:
    print(f'{row['no']}\t{row['name']}\t{row['email']}\t{row['password']}\t{row['gender']}\t{row['delYn']}\t{row['regDate']}\t{row['modDate']}')

def boardDetail(args):
  sql=f'''
      select post.no, post.title, post.content, user.name, post.regDate, post.modDate
      from team2.post
      inner join team2.user
      on (post.user_no = `user`.no)
      where post.`delYn` = 0 and post.`no` = {args.no}
      '''
  print(f'번호\t제목\t내용\t글작성자\t글작성일자\t글수정일자')
  print('-'*50)
  list = findAll(sql)
  for row in list:
    print(f'{row['no']}\t{row['title']}\t{row['content']}\t{row['name']}\t{row['regDate']}\t{row['modDate']}')\
    

def userEdit(args):
  sql = f'''
        update team2.user set `{args.key}` = '{args.value}'
        where user.no = {args.no}
        '''
  save(sql)
  userList(None)

def boardEdit(args):
  sql = f'''
       update team2.post set `{args.key}` = '{args.value}'
        where post.no = {args.no}
        '''
  save(sql)
  boardList(None)

  
def userDelete(args):
  sql = f'''
        update team2.user set `delYn` = True
        where user.no = {args.no}
        '''
  save(sql)
  userList(None)

def boardDelete(args):
  sql = f'''
        update team2.post set `delYn` = True
        where post.no = {args.no}
        '''
  save(sql)
  boardList(None)