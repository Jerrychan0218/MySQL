SHOW DATABASES;
USE `sql_tutorial`;
DROP TABLE `student`;

#創建資料庫
CREATE TABLE `employee`(
	`emp_id` INT PRIMARY KEY,
    `name` VARCHAR(20),
    `birth_date` DATE,
    `sex` VARCHAR(1),
    `salary` INT,
    `branch_id` INT,
    `sup_id` INT
);

CREATE TABLE `branch`(
	`branch_id` INT PRIMARY KEY,
    `branch_name` VARCHAR(20),
    `manager_id` INT,
    FOREIGN KEY (`manager_id`) REFERENCES `employee`(`emp_id`) ON DELETE SET NULL # ON DELETE SET NULL是指當emp_id被刪掉，manager_id就會NULL
);

ALTER TABLE `employee`
ADD FOREIGN KEY(`branch_id`) REFERENCES `branch`(`branch_id`) ON DELETE SET NULL;

ALTER TABLE `employee`
ADD FOREIGN KEY(`sup_id`) REFERENCES `employee`(`emp_id`) ON DELETE SET NULL;

CREATE TABLE `client`(
	`client_id` INT PRIMARY KEY,
    `client_name` VARCHAR(20),
    `phone` VARCHAR(20)
);

CREATE TABLE `work_with`(
	`emp_id` INT,
    `client_id` INT,
    `total_sale` INT,
    PRIMARY KEY(`emp_id`, `client_id`),
    FOREIGN KEY(`emp_id`) REFERENCES `employee`(`emp_id`) ON DELETE CASCADE, # ON DELETE CASCADE是指當emp_id被刪掉，WORK_WITH中對應的emp_id就會同樣被刪掉
    FOREIGN KEY(`client_id`) REFERENCES `client`(`client_id`) ON DELETE CASCADE # 補充一下，foreign key 同時是primary key時就不可以set NULL
);
#新增資料進去資料庫

INSERT INTO `branch` VALUES(1, '行政', NULL);
INSERT INTO `branch` VALUES(2, '研發', NULL);
INSERT INTO `branch` VALUES(3, '分析', NULL);

INSERT INTO `employee` VALUES(206, '小豪', '1995-02-18', 'M', 50000, 3, NULL);
INSERT INTO `employee` VALUES(207, '小黃', '1996-08-18', 'F', 45000, 1, 207);
INSERT INTO `employee` VALUES(208, '小藍', '1996-09-27', 'F', 48000, 1, 207);
INSERT INTO `employee` VALUES(209, '小泓', '1996-09-30', 'M', 55000, 2, 206);
INSERT INTO `employee` VALUES(210, '小謙', '1996-06-14', 'M', 57000, 2, 206);

INSERT INTO `client` VALUES(400, '阿狗', '2210223');
INSERT INTO `client` VALUES(401, '阿喵', '2200222');
INSERT INTO `client` VALUES(402, '阿玆', '3342225');
INSERT INTO `client` VALUES(403, '阿玄', '2559793');
INSERT INTO `client` VALUES(404, '阿峰', '2800082');

INSERT INTO `work_with` VALUES(206, 400, 59699);
INSERT INTO `work_with` VALUES(206, 401, 42220);
INSERT INTO `work_with` VALUES(207, 402, 30005);
INSERT INTO `work_with` VALUES(208, 403, 50000);
INSERT INTO `work_with` VALUES(209, 404, 90000);

#修改資料
UPDATE `branch`
SET `manager_id` = 207
WHERE `branch_id` = 1;

#取得資料
#全部員工
SELECT * FROM `employee`;
#全部顧客
SELECT * FROM `client`;
#按薪水低到高顯示所有員工資料
SELECT * FROM `employee` ORDER BY `salary`;
#顯示薪水最高的三位員工
SELECT * FROM `employee` ORDER BY `salary` DESC LIMIT 3; 
#取得員工名字
SELECT `name` FROM `employee`;
#取得部門序號
SELECT DISTINCT `branch_id` FROM `employee`; #加了DISTINCT後就不會顯示重複的值
 