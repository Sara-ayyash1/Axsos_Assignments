# User Dashboard ERD
Entity Relationship Diagram for a user dashboard web application built with MySQL Workbench. The platform allows users to register, manage their profiles, write messages on other users' profiles (similar to a Facebook Wall), and reply to those messages via comments.

##  Wireframe Analysis
The wireframe revealed two core interactions:
1. **Profile Messages:** A user can write a message on another user's profile page — requiring a `sender_id` (who wrote it) and a `receiver_id` (whose profile it's on).
2. **Message Replies (Comments):** Other users can reply to any message on a profile — requiring a `comments` table linked to both the message and the user who replied.

> Note: Messages are not public posts — they are written on a specific user's profile, similar to the old Facebook Wall feature.

##  Key Concepts
- **Self-Referencing via sender/receiver:** The `messages` table references `users` twice — once as `sender_id` and once as `receiver_id` — both pointing to the same `users` table.
- **One-to-Many (messages → comments):** Each message can have multiple replies.
- **User Levels:** The `user_level` column in `users` determines access (admin or normal). The first user to register becomes admin automatically.
- **Admin Privileges:** Only admins can add, edit, or remove other users.

## Tables

### users
| Column | Type | Notes |
|--------|------|-------|
| user_id | INT | Primary Key |
| first_name | VARCHAR(45) | |
| last_name | VARCHAR(45) | |
| email | VARCHAR(45) | |
| password | VARCHAR(45) | |
| user_level | VARCHAR(45) | "admin" or "normal" |
| created_at | DATETIME | |

### messages
| Column | Type | Notes |
|--------|------|-------|
| message_id | INT | Primary Key |
| content | VARCHAR(255) | |
| created_at | DATETIME | |
| sender_id | INT | Foreign Key → users (who wrote it) |
| receiver_id | INT | Foreign Key → users (whose profile) |

### comments
| Column | Type | Notes |
|--------|------|-------|
| comment_id | INT | Primary Key |
| content | VARCHAR(255) | |
| created_at | DATETIME | |
| user_id | INT | Foreign Key → users |
| message_id | INT | Foreign Key → messages |

##  Relationships
- A **user** can send many **messages** (one-to-many via sender_id)
- A **user** can receive many **messages** (one-to-many via receiver_id)
- A **message** can have many **comments/replies** (one-to-many)
- A **user** can write many **comments** (one-to-many)


##  How to Open Locally
1. Open MySQL Workbench
2. Go to **File → Open Model**
3. Select the `.mwb` file
4. Click **Add Diagram** to view the ERD