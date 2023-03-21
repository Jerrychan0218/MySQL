# WILDCARDS 萬用字元 %代表多個字元, _ 代表一個字元
USE `sql_tutorial`;
SELECT * FROM `employee`;
#取得電話號碼尾數為335的客戶
SELECT * FROM `client` WHERE `phone` LIKE '%223'; # %335的意思就是不管前面的數字是甚麼，只要尾數是335就符合要求
#取得姓阿的客戶
SELECT * FROM `client` WHERE `client_name` LIKE '阿%';
#取得生日為2月的員工
SELECT * FROM `employee` WHERE `birth_date` LIKE '_____02%';

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
    FOREIGN KEY (`manager_id`) REFERENCES `employee`(`emp_id`) ON DELETE SET NULL 
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
    FOREIGN KEY(`emp_id`) REFERENCES `employee`(`emp_id`) ON DELETE CASCADE,
    FOREIGN KEY(`client_id`) REFERENCES `client`(`client_id`) ON DELETE CASCADE
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