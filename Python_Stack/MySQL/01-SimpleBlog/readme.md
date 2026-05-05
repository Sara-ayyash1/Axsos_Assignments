# Simple Blog ERD
Entity Relationship Diagram for a simple blogging platform built with MySQL Workbench. Users can register, create posts, and leave comments on posts. The schema was derived by analyzing the wireframe showing a login/registration page and a posts page with comments.

##  Wireframe Analysis
The wireframe shows:
- **Login / Registration** → `users` table
- **Posts page** with "Posted by: Andrew, 3 hours ago" → `posts` table with `user_id` and `created_at`
- **Comments section** with "Posted by: Kobe, 2 hours ago" → `comments` table with `user_id`, `post_id`, and `created_at`

##  Key Concepts
- **One-to-Many (users → posts):** A user can create many posts.
- **One-to-Many (posts → comments):** A post can have many comments.
- **One-to-Many (users → comments):** A user can write many comments.

##  Tables

### users
| Column | Type | Notes |
|--------|------|-------|
| user_id | INT | Primary Key |
| email | VARCHAR(255) | |
| password | VARCHAR(45) | |

### posts
| Column | Type | Notes |
|--------|------|-------|
| post_id | INT | Primary Key |
| content | LONGTEXT | |
| created_at | DATETIME | |
| user_id | INT | Foreign Key → users |

### comments
| Column | Type | Notes |
|--------|------|-------|
| comment_id | INT | Primary Key |
| content | LONGTEXT | |
| created_at | DATETIME | |
| user_id | INT | Foreign Key → users |
| post_id | INT | Foreign Key → posts |

##  Relationships
- A **user** can write many **posts** (one-to-many)
- A **post** can have many **comments** (one-to-many)
- A **user** can write many **comments** (one-to-many)
