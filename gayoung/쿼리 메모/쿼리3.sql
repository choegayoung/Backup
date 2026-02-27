information_schemaSELECT * FROM edu.study;

INSERT INTO edu.study (`word`) VALUE ('테스트');

COMMIT;

UPDATE edu.study SET `word` = '' WHERE `id` = 0;

DELETE FROM edu.study WHERE `id` = 0 ;

CREATE TABLE `edu`.`user`(
    `no`              INT                 NOT NULL    COMMENT '번호'     AUTO_INCREMENT PRIMARY KEY,
    `name`          VARCHAR(20)     NOT NULL    COMMENT '이름',
    `email`          VARCHAR(255)     NOT NULL    COMMENT '이메일',
    `password`     VARCHAR(255)     NOT NULL    COMMENT '비밀번호',
    `gender`        BOOLEAN            NULL        COMMENT '성별(0:여자, 1:남자)',
    `delYn`        BOOLEAN            NOT NULL COMMENT '탈퇴여부(0:회원, 1: 탈퇴)`'    DEFAULT FALSE,
    `regDate`     DATETIME        NOT NULL COMMENT '회원등록일자'            DEFAULT CURRENT_TIMESTAMP,
    `modDate`     DATETIME        NOT NULL COMMENT '회원정보수정일자'    DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE `edu`.`gayounguser`(
	`no`	INT	NOT NULL	COMMENT'번호' AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(20) NOT NULL COMMENT'이름',
	`email` VARCHAR(255) NOT NULL COMMENT'이메일',
	`password` VARCHAR(255) NOT NULL COMMENT'비밀번호',
	`gender` BOOLEAN NULL COMMENT'성별(0:여자, 1:남자)' DEFAULT FALSE,
	`delYn` BOOLEAN NOT NULL COMMENT'탈퇴여부(0:회원, 1:탈퇴)' DEFAULT FALSE,
	`regDate` DATETIME NOT NULL COMMENT'회원등록일자' DEFAULT CURRENT_TIMESTAMP,
	`modDate` DATETIME NOT NULL COMMENT'회원정보수정일자' DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
	);

CREATE TABLE `edu`.`gayoungboard`(
	`no`	INT	NOT NULL	COMMENT'게시글번호' AUTO_INCREMENT PRIMARY KEY,
	`title` VARCHAR(20) NOT NULL COMMENT'제목',
	`content` VARCHAR(255) NOT NULL COMMENT'내용',
	`delYn` BOOLEAN NULL COMMENT'삭제여부(0:존재, 1:삭제)' DEFAULT FALSE,
	`writer_no`	INT	NOT NULL	COMMENT'작성자번호',
	`regDate` DATETIME NOT NULL COMMENT'글작성일자' DEFAULT CURRENT_TIMESTAMP,
	`modDate` DATETIME NOT NULL COMMENT'글수정일자' DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	
	CONSTRAINT fk_gayoungboard_writer
	FOREIGN KEY (writer_no)
	REFERENCES edu.gayounguser(no)

);

SELECT * FROM team2.`user`
WHERE `delYn` = 0;

SELECT post.title, post.content, user.`name` FROM team2.post
INNER JOIN team2.`user`
ON `user`.no = post.user_no
WHERE post.delYn = 0;

INSERT INTO team2.`user`
(name, email, password, gender)
VALUES ('가영', '가영메일', '123', 0);

INSERT INTO team2.post
(title, content, user_no)
VALUES ('가영제목','가영글',2);

UPDATE team2.`user` SET `user`.`name` = '가아영'
WHERE `no` = 14;

SHOW PROCESSLIST;

SELECT * FROM team2.`user`
WHERE user.no = 13;