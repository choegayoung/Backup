CREATE TABLE test(
  `no` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(20) NOT NULL,
  `regdate` DATETIME NOT NULL 
); ## 새 테이블 만들기 


SELECT * FROM edu.test;

INSERT INTO edu.test 
(`name`, `regDate`) 
VALUE ('ㅇㅇ',NOW()) ;

COMMIT;

UPDATE edu.test SET `name` = '졸려요' WHERE `no` = '6';

ROLLBACK;

DELETE FROM edu.test WHERE `no` = 5; # 번호는 초기화 안됨

DROP TABLE test; ## 테이블을 몽땅 지우고 초기화 할 때

TRUNCATE edu.test; ## 대상 테이블이 있을 때, drop => create
