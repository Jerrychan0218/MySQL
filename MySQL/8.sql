USE `sql_tutorial`;

#subquery 子查詢

#找出研發部門的經理名字
SELECT `name` FROM `employee` WHERE `emp_id` = (SELECT `manager_id` FROM `branch` WHERE `branch_name` = '研發'); # =只能回一筆資料


#找出單客戶銷售額就超50000的員工名字
SELECT `name` FROM `employee` WHERE `emp_id` in (SELECT `emp_id` FROM `work_with` WHERE `total_sale` > 50000); # IN可以回很多資料

