USE `sql_tutorial`;

CREATE TABLE `notification_clicked`(
	`event` VARCHAR(20),
    `product` VARCHAR(20),
    `memberId` INT PRIMARY KEY UNIQUE,
    `createdAt` DATE
); 

DESCRIBE `notification_clicked`;
INSERT INTO `notification_clicked` VALUES ("notification_clicked", 'super', 1, '2022/2/18');
INSERT INTO `notification_clicked` VALUES ("notification_clicked", 'hi', 2, '2022/3/6');
INSERT INTO `notification_clicked` VALUES ("notification_clicked", 'i', 3, '2022/4/22');
INSERT INTO `notification_clicked` VALUES ("notification_clicked", 'am', 4, '2022/5/4');
INSERT INTO `notification_clicked` VALUES ("notification_clicked", 'jerry', 5, '2022/6/8');
INSERT INTO `notification_clicked` VALUES ("notification_clicked", 'nice', 6, '2022/7/1');
INSERT INTO `notification_clicked` VALUES ("notification_clicked", 'to', 7, '2022/8/9');
INSERT INTO `notification_clicked` VALUES ("notification_clicked", 'meet', 8, '2022/9/6');
INSERT INTO `notification_clicked` VALUES ("notification_clicked", 'you', 9, '2022/10/7');
INSERT INTO `notification_clicked` VALUES ("notification_clicked", 'here', 10, '2022/11/8');

SELECT * FROM `notification_clicked`;

CREATE TABLE `ec_purchased`(
	`event` VARCHAR(20),
    `product` VARCHAR(20),
    `memberId` INT PRIMARY KEY UNIQUE,
    `createdAt` DATE
); 

INSERT INTO `ec_purchased` VALUES ("ec_purchased", 'super', 1, '2022/2/18');
INSERT INTO `ec_purchased` VALUES ("ec_purchased", 'hi', 2, '2022/6/18');
INSERT INTO `ec_purchased` VALUES ("ec_purchased", 'i', 3, '2022/6/18');
INSERT INTO `ec_purchased` VALUES ("ec_purchased", 'd', 4, '2022/6/18');
INSERT INTO `ec_purchased` VALUES ("ec_purchased", 'c', 5, '2022/10/18');
INSERT INTO `ec_purchased` VALUES ("ec_purchased", 't', 6, '2022/12/7');
INSERT INTO `ec_purchased` VALUES ("ec_purchased", 'y', 7, '2022/9/7');
INSERT INTO `ec_purchased` VALUES ("ec_purchased", 'y', 8, '2022/10/11');
INSERT INTO `ec_purchased` VALUES ("ec_purchased", 'you', 9, '2022/12/18');
INSERT INTO `ec_purchased` VALUES ("ec_purchased", 'super', 10, '2022/11/18');

SELECT memberId, COUNT(ec_purchased.event)/COUNT(notification_click.event) where 

