SHOW DATABASES;
CREATE DATABASE `test`;
USE `test`;

SET SQL_SAFE_UPDATES = 0;

CREATE TABLE `student`(
	`student_id` INT PRIMARY KEY auto_increment, 
    `name` VARCHAR(20),
    `major` VARCHAR(20),
    `score` INT
    #PRIMARY KEY(`student_id); 這樣也可以，但上面的`student_id` INT PRIMARY KEY, 就要改成`student_id` INT
); 

DROP TABLE `student`;

SELECT * FROM `student`; #要搜尋stutdent裡的所有資料

INSERT INTO `student`(`name`, `major`, `score`) VALUES ('Jerry', '化學', 86); 

UPDATE `student` #我們要更新資料
SET `name` = 'patrick', `major` = '化學' #我要更新成jerry 以及化學
#WHERE `major` = '英國文學' or `major` = '數學' #把所有major column裡的ENG
WHERE `student_id` = 3; #如果不加where就會把所有資料的major改成化學

DELETE FROM `student`
WHERE `name` = 'Jerry';
