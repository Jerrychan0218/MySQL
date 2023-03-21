#aggregate function 聚合函數

USE `sql_tutorial`;

#取得員工人數
SELECT COUNT(*) FROM `employee`; #*號可以用其他variance代替

#取得所有出生於1970-01-01之後的女性員工
SELECT COUNT(*) FROM `employee` WHERE `birth_date` > '1970-01-01' AND `sex` = 'F';

#員工平均薪水
SELECT AVG(`salary`) FROM `employee`;

#員工薪水總和
SELECT SUM(`salary`) FROM `employee`;

#薪水最高的員工
SELECT max(`salary`) FROM `employee`;

#薪水最低的員工
SELECT min(`salary`) FROM `employee`;
