USE `sql_tutorial`;
SELECT * FROM `work_with`;
#UNION 聯集

# UNION客戶名字，合併要column數一樣，資料屬性也要一樣
SELECT `name` FROM `employee`
UNION #可以把兩個column的東西合併在一起呈現
SELECT `client_name` FROM `client`
UNION
SELECT `branch_name` FROM `branch`;

# 員工ID+員工名字 Union 客戶ID + 客戶名字
SELECT `emp_id` AS `all_id`, `name` AS `all_name` FROM `employee` #如果不加as的話，就會使用emp_id、name作為column名字
UNION
SELECT `client_id`, `client_name` FROM `client`;

#員工薪水 union 銷售金額
SELECT `salary` AS `total_money`FROM `employee`
UNION
SELECT `total_sale` FROM `work_with`;

SELECT * FROM `branch`;
INSERT INTO `branch` VALUES(4, '偷懶', NULL);

#join 連接

#取得部門經理的名字
SELECT * FROM `employee` join `branch` ON `emp_id` = `manager_id`;
SELECT `emp_id`, `name`, `branch_name` FROM `employee` join `branch` ON `employee`.`emp_id` = `branch`.`manager_id`; # `employee`.`emp_id` 有一點就可以避免當初可能有兩個table是同名的狀況，讓sql分辨得出來
#left join 無論條件有沒有成立，都會回傳左邊的table 也就是employee，右邊表只有在合乎條件的情況下才會出現。
SELECT `emp_id`, `name`, `branch_name` FROM `employee` left join `branch` ON `employee`.`emp_id` = `branch`.`manager_id`;

