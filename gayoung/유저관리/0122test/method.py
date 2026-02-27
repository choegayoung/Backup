from db import findAll, save

def list(args):
    sql='''
    SELECT * FROM edu.`user`
    WHERE `delYn`=0;
    '''
    arr = findAll(sql)
    print(f'번호\t이름\t이메일\t비번\t성별\t회원등록일자\t회원정보수정일자')
    print("-"*85)
    for row in arr:
        print(f'{row["no"]}\t{row['name']}\t{row['email']}\t{row['password']}\t{row['gender']}\t{row['regDate']}\t{row['modDate']}')

def add(args):
    sql=f'''
    INSERT INTO edu.`user` (`name`,`email`,`password`,`gender`) 
    VALUES('{args.name}','{args.email}','{args.pwd}',{args.gender});
    '''
    save(sql)
    list(None)

def select(args):
    sql=f'''
    SELECT * FROM edu.`user`
    WHERE `no`={args.no};'''
    arr = findAll(sql)
    print(f'번호\t이름\t이메일\t비번\t성별\t탈퇴여부\t회원등록일자\t회원정보수정일자')
    print("-"*95)
    for row in arr:
        print(f'{row["no"]}\t{row['name']}\t{row['email']}\t{row['password']}\t{row['gender']}\t{row['delYn']}\t{row['regDate']}\t{row['modDate']}')

def update(args):
    sql=f'''
    UPDATE edu.`user` SET `{args.key}` = '{args.value}'
    WHERE `no` = {args.no}
    '''
    save(sql)
    list(None)

def quit(args):
    
    sql=f'''
    UPDATE edu.`user` SET `delYn` = 1
    WHERE `no` = {args.no};
    '''
    save(sql)
    list(None)

# def zagaip(args):
#     sql=f'''
#     UPDATE edu.`user` SET `delYn` = 0
#     WHERE `no` = {args.no};
#     '''
#     save(sql)
#     list(None)
