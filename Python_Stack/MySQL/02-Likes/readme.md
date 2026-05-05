# Likes ERD
Entity Relationship Diagram for a social media post system with likes and comments, built with MySQL Workbench. Users can create posts with photos, like posts, and comment on them. The schema was derived from a Facebook-style wireframe showing a post with like, comment, and share actions.

##  Wireframe Analysis
The wireframe shows:
- A **post** with text content and a photo → `posts` table with `content`, `post_photo_url`, `user_id`
- **Like · Comment · Share** actions → `likes` join table (many-to-many between users and posts)
- **Comments** section → `comments` table linked to post and user
- "4 likes" count → calculated from `likes` table, not stored directly

##  Key Concepts
- **Many-to-Many (users ↔ posts via likes):** A user can like many posts, and a post can be liked by many users — resolved via the `likes` join table.
- **One-to-Many (posts → comments):** A post can have many comments.
- **One-to-Many (users → comments):** A user can write many comments.
- **Singular Foreign Keys:** Foreign keys follow singular naming (post_id, user_id) as required by the assignment.

##  Tables

### users
| Column | Type | Notes |
|--------|------|-------|
| user_id | INT | Primary Key |
| name | VARCHAR(45) | |
| email | VARCHAR(45) | |

### posts
| Column | Type | Notes |
|--------|------|-------|
| post_id | INT | Primary Key |
| content | LONGTEXT | |
| post_photo_url | VARCHAR(255) | |
| created_at | DATETIME | |
| user_id | INT | Foreign Key → users |

### likes *(join table)*
| Column | Type | Notes |
|--------|------|-------|
| id | INT | Primary Key |
| post_id | INT | Foreign Key → posts |
| user_id | INT | Foreign Key → users |

### comments
| Column | Type | Notes |
|--------|------|-------|
| comment_id | INT | Primary Key |
| content | LONGTEXT | |
| created_at | DATETIME | |
| post_id | INT | Foreign Key → posts |
| user_id | INT | Foreign Key → users |

##  Relationships
- A **user** can create many **posts** (one-to-many)
- A **user** can like many **posts**, and a **post** can be liked by many **users** (many-to-many via `likes`)
- A **post** can have many **comments** (one-to-many)
- A **user** can write many **comments** (one-to-many)

