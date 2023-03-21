CREATE DATABASE `sql_tutorial`; #創建
SHOW DATABASES; #展示有啥database
USE `sql_tutorial`; #用哪一個database

CREATE TABLE `student`(
	`student_id` INT PRIMARY KEY AUTO_INCREMENT, #INT 是字串，PRIMARY KEY 就是可以用來辨別每筆資料的COLUMN 研究常用ID，AUTO_INCREMENT就可以自動幫你加一
    `name` VARCHAR(20) NOT NULL, #NOT NULL 是一種CONSTRAINT 限制，代表不能是空的 
    `major` VARCHAR(20) UNIQUE # UNIQUE也是一種constraint，代表不能有重複值
    #PRIMARY KEY(`student_id); 這樣也可以，但上面的`student_id` INT PRIMARY KEY, 就要改成`student_id` INT
); 

DESCRIBE `student`; #展示student
DROP TABLE `student`; #刪除都是drop

ALTER TABLE `student` ADD gpa DECIMAL(3,2) DEFAULT(2.50); #Alter 改變，decimal = 小數點
ALTER TABLE `student` DROP COLUMN gpa;

SELECT * FROM `student`; #要搜尋stutdent裡的所有資料

INSERT INTO `student` VALUES(1, '小黑', '生物', NULL); #存資料進STUDENT，跟PYTHON一樣，字串要''
INSERT INTO `student`(`name`, `major`, `gpa`) VALUES ('小黑', '生物', 4.02);
