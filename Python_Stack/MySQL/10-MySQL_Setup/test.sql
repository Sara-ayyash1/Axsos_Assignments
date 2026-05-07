CREATE DATABASE test_db;
USE test_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

INSERT INTO students (name, age) VALUES ('Sara', 21);

SELECT * FROM students;

UPDATE students SET age = 21 WHERE id = 1;

DELETE FROM students WHERE id = 1;