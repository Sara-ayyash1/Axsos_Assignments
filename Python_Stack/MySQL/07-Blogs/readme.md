# Blog System ERD

##  Requirements Analysis
- User registration and authentication
- Users creating multiple blogs
- Inviting other users as **co-administrators** of a blog
- Blog admins managing: blog name, posts, comments, and file uploads
- Tracking page view analytics (page visited, time, duration, IP address, user name)

Each requirement mapped directly to a database table.

## Key Concepts
- **One-to-Many:** A user can own many blogs. A blog can have many posts. A post can have many comments and many files.
- **Many-to-Many:** A blog can have multiple admins, and a user can admin multiple blogs → resolved via the `blog_admin` join table.
- **Analytics Table:** The `page_view` table captures user browsing behavior per session (page, time, duration, IP).
- **Separation of Concerns:** Each entity (posts, comments, files, admins) has its own table to avoid redundancy and maintain scalability.

##  Tables

### users
| Column | Type | Notes |
|--------|------|-------|
| user_id | INT | Primary Key |
| username | VARCHAR(45) | |
| email | VARCHAR(200) | |
| password | VARCHAR(45) | |

### blogs
| Column | Type | Notes |
|--------|------|-------|
| blog_id | INT | Primary Key |
| name | VARCHAR(45) | |
| user_id | INT | Foreign Key → users (owner) |

### blog_admin *(join table)*
| Column | Type | Notes |
|--------|------|-------|
| admin_id | INT | Primary Key |
| blog_id | INT | Foreign Key → blogs |
| user_id | INT | Foreign Key → users |

### posts
| Column | Type | Notes |
|--------|------|-------|
| post_id | INT | Primary Key |
| title | VARCHAR(45) | |
| content | LONGTEXT | |
| blog_id | INT | Foreign Key → blogs |

### comments
| Column | Type | Notes |
|--------|------|-------|
| comment_id | INT | Primary Key |
| content | TEXT | |
| post_id | INT | Foreign Key → posts |
| user_id | INT | Foreign Key → users |

### files
| Column | Type | Notes |
|--------|------|-------|
| file_id | INT | Primary Key |
| file_path | VARCHAR(45) | |
| ... | | 2 more columns (not fully visible) |

### page_view
| Column | Type | Notes |
|--------|------|-------|
| id | INT | Primary Key |
| page_visited | TINYINT | |
| visited_at | DATETIME | |
| duration_of_visit | TIME | |
| ip_address | VARCHAR(45) | |
| name | VARCHAR(45) | |
| user_id | INT | Foreign Key → users |

##  Relationships
- A **user** can own many **blogs** (one-to-many)
- A **blog** can have many **co-admins** via `blog_admin` (many-to-many)
- A **blog** can have many **posts** (one-to-many)
- A **post** can have many **comments** (one-to-many)
- A **post** can have many **files** (one-to-many)
- A **user** can have many **page views** tracked (one-to-many)


##  How to Open Locally 
1. Open MySQL Workbench
2. Go to **File → Open Model**
3. Select the `blog_system_ERD.mwb` file
4. Click **Add Diagram** to view the ERD