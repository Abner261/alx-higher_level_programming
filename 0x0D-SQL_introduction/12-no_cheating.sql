-- A script that updates the score of Bob to 10 in the table second_table
--
-- score   name
-- 10      Bob
-- 10      John
-- 8       George
-- 3       Alex

UPDATE second_table SET `score` = 10 WHERE `name` = 'Bob';
