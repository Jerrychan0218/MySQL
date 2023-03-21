SELECT * FROM `student` ORDER BY `score`, `student_id` DESC; # * 是所有東西的意思，order by 是排列，這邊先用score排，再用student_id排(如果score有一樣的話)，DESC 就是由高至低排序，ASC就是由低到高
SELECT `name` FROM `student`;  #也可以只拿其中的東西出來
SELECT * FROM `student` ORDER BY `score` DESC LIMIT 3; #LIMIT 回傳的筆數，先排序後回傳也可
SELECT * FROM `student` WHERE `major` = '數學';
SELECT * FROM `student` WHERE `major` = '數學' or `major` = '化學';
SELECT * FROM `student` WHERE `major` in ('數學', '化學'); #這個跟第5行是一樣的東西

INSERT INTO `student` values(5, 'jenny', '化學', 100);

update `student`
set `major` = '數學'
where `student_id` in (2);

select * from `student`