-- SELF JOIN => Join anather copy of a table to itself
use mydb;
-- Query: Create 6 new users
INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('Amy', 'Giver', NOW(), NOW()),
('Eli', 'Byers', NOW(), NOW()),
('Big', 'Bird', NOW(), NOW()),
('Kermit', 'The Frog', NOW(), NOW()),
('Marky', 'Mark', NOW(), NOW()),
('Sara', 'Ayyash', NOW(), NOW());

-- Query: Have user 1 be friends with users 2, 4, and 6
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (1, 2, NOW(), NOW()), 
(1, 4, NOW(), NOW()),
(1, 6, NOW(), NOW()); 

-- Query: Have user 2 be friends with users 1, 3, and 5
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (2, 1, NOW(), NOW()), 
(2, 3, NOW(), NOW()),
(2, 5, NOW(), NOW());

-- Query: Have user 3 be friends with users 2 and 5
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (3, 2, NOW(), NOW()),
(3, 5, NOW(), NOW());

-- Query: Have user 4 be friends with user 3
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (4, 3, NOW(), NOW()) ;

-- Query: Have user 5 be friends with users 1 and 6
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (5, 1, NOW(), NOW()), (5, 6, NOW(), NOW());

-- Query: Have user 6 be friends with users 2 and 3
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (6, 2, NOW(), NOW()), (6, 3, NOW(), NOW()); 

-- Query: Display the relationships created as shown in the above image
SELECT U.first_name , U.last_name , user2.first_name as friend_first_name, user2.last_name as friend_last_name
FROM users AS U JOIN friendships AS F
ON U.USER_ID = F.USER_ID
LEFT JOIN users as user2 ON F.friend_id = user2.USER_ID;

-- NINJA Query: Return all users who are friends with the first user, and make sure their names are displayed in the results.
SELECT U.first_name , U.last_name 
FROM users AS U JOIN friendships AS F
ON U.USER_ID = F.USER_ID
where F.FRIEND_ID =1 ;

-- NINJA Query: Return the count of all friendships
SELECT count(friend_id) as total_friendships
FROM friendships ;

-- NINJA Query: Find out who has the most friends and return the count of their friends.
SELECT u.user_id, U.first_name , U.last_name ,count(f.friend_id) as friends_count
FROM users AS U JOIN friendships AS F
ON U.USER_ID = F.USER_ID
group by user_id
having friends_count = (select count(friend_id) from friendships group by user_id order by count(friend_id) desc Limit 1);

-- NINJA Query: Return the friends of the third user in alphabetical order
SELECT u.user_id, U.first_name , U.last_name ,f.friend_id ,concat(user2.first_name, " ", user2.last_name) as friend_name
FROM users AS U JOIN friendships AS F
ON U.USER_ID = F.USER_ID
join users as user2
on user2.user_id = f.friend_id
where u.user_id = 3
order by friend_name