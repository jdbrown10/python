-- ====== SELECT ======
-- SELECT * FROM users ORDER BY birthday DESC;

-- SELECT * FROM users WHERE first_name LIKE "%e%" ORDER BY first_name ASC;

-- SELECT * FROM tweets WHERE user_id = 2 ORDER BY id DESC LIMIT 3;

-- ====== INSERT ======
-- Template:
-- INSERT INTO table_name (column_name1, column_name2) 

-- VALUES('column1_value', 'column2_value');
-- DON'T insert into existing IDs, just auto increment

-- INSERT INTO users (birthday, first_name, last_name, handle, created_at, updated_at) 
-- VALUES('1998-03-13', 'Bobothy', 'Jones', 'bobbyj2019', NOW(), NOW());

-- ====== UPDATE ======
-- Template:
-- UPDATE table_name SET column_name1 = 'some_value', column_name2='another_value' WHERE condition(s)

-- the "where" condition is almost always an ID because it's guaranteed to be unique!
-- ALWAYS update the updated_at column
-- don't forget the commas between values

-- UPDATE users SET first_name = 'jimothy', handle='jimmyJ2019', updated_at = NOW(), birthday='1998-03-13' WHERE id=6

-- ====== DELETE ======
-- Template:
-- DELETE FROM table_name WHERE condition

-- never touch the ID of something you deleted-- once you delete 7, don't touch id 7 again. If you do it's gonna be bad news.

-- DELETE FROM users WHERE id= 7;




