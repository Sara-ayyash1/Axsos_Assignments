# SQL Self Join Assignment

## Overview

This assignment demonstrates the concept of **Self Join** in SQL — joining a table to another copy of itself. The project uses a `users` table and a `friendships` table to simulate a social network where users can have friendships with each other.

---

## Database

```sql
USE mydb;
```

---

## Tables Used

| Table         | Description                              |
|---------------|------------------------------------------|
| `users`       | Stores user information (name, timestamps) |
| `friendships` | Stores friendship relationships between users |

---

## Setup — Insert Data

### Create 6 Users

```sql
INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('Amy', 'Giver', NOW(), NOW()),
       ('Eli', 'Byers', NOW(), NOW()),
       ('Big', 'Bird', NOW(), NOW()),
       ('Kermit', 'The Frog', NOW(), NOW()),
       ('Marky', 'Mark', NOW(), NOW()),
       ('Sara', 'Ayyash', NOW(), NOW());
```

### Create Friendships

| User       | Friends With       |
|------------|--------------------|
| User 1     | Users 2, 4, 6      |
| User 2     | Users 1, 3, 5      |
| User 3     | Users 2, 5         |
| User 4     | User 3             |
| User 5     | Users 1, 6         |
| User 6     | Users 2, 3         |

---

## Queries

### 1. Display All Friendships (Self Join)

Joins the `users` table to itself through the `friendships` table to display each user alongside their friend's name.

```sql
SELECT U.first_name, U.last_name,
       user2.first_name AS friend_first_name,
       user2.last_name  AS friend_last_name
FROM users AS U
JOIN friendships AS F ON U.user_id = F.user_id
LEFT JOIN users AS user2 ON F.friend_id = user2.user_id;
```

---

### 2.  Ninja — Users Who Are Friends With User 1

Returns all users who have user 1 listed as their friend.

```sql
SELECT U.first_name, U.last_name
FROM users AS U
JOIN friendships AS F ON U.user_id = F.user_id
WHERE F.friend_id = 1;
```

---

### 3.  Ninja — Total Friendship Count

Returns the total number of friendship records in the table.

```sql
SELECT COUNT(friend_id) AS total_friendships
FROM friendships;
```

---

### 4.  Ninja — User With the Most Friends

Finds which user has the highest number of friends and returns their info along with that count.

```sql
SELECT u.user_id, U.first_name, U.last_name,
       COUNT(f.friend_id) AS friends_count
FROM users AS U
JOIN friendships AS F ON U.user_id = F.user_id
GROUP BY user_id
HAVING friends_count = (
    SELECT COUNT(friend_id)
    FROM friendships
    GROUP BY user_id
    ORDER BY COUNT(friend_id) DESC
    LIMIT 1
);
```

---

### 5.  Ninja — Friends of User 3 in Alphabetical Order

Returns the friends of the third user, sorted alphabetically by full name.

```sql
SELECT u.user_id, U.first_name, U.last_name,
       f.friend_id,
       CONCAT(user2.first_name, ' ', user2.last_name) AS friend_name
FROM users AS U
JOIN friendships AS F ON U.user_id = F.user_id
JOIN users AS user2 ON user2.user_id = F.friend_id
WHERE u.user_id = 3
ORDER BY friend_name;
```

---

## Key Concepts

- **Self Join**: Joining a table to a copy of itself using aliases (`U`, `user2`) to represent different roles (user vs. friend).
- **LEFT JOIN**: Used to include users even if they have no matching friend record.
- **Subquery in HAVING**: Used to dynamically find the maximum friend count without hardcoding a value.
- **CONCAT**: Combines first and last name into a single readable field.
- **GROUP BY + HAVING**: Aggregates friendship counts per user and filters by a condition on the aggregate.