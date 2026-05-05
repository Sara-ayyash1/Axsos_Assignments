# Belt Certifications ERD
Entity Relationship Diagram for a belt certification tracking system built with MySQL Workbench. The platform tracks students and their earned belt levels (e.g. yellow, red, black). Since a student can earn multiple belts and a belt can be earned by multiple students, a many-to-many relationship was implemented using a join table.

##  Wireframe Analysis
The wireframe shows a table with:
- **Name** column → `users` table
- **Belts** column showing multiple belts per student (e.g. "yellow red black") → each belt is a separate record

This means one student can have many belts → **many-to-many relationship** between `users` and `belts`.

##  Key Concepts
- **Many-to-Many Relationship:** A user can earn many belts, and a belt type can be earned by many users — resolved via the `users_belts` join table.
- **Temporal Tracking:** `created_at` in `users_belts` tracks when each belt was earned. `created_at` and `updated_at` in both `users` and `belts` for record management.
- **Join Table:** `users_belts` holds only the two foreign keys plus the earned date — keeping data normalized.

##  Tables

### users
| Column | Type | Notes |
|--------|------|-------|
| id | INT | Primary Key |
| first_name | VARCHAR(45) | |
| last_name | VARCHAR(45) | |
| created_at | DATETIME | |
| updated_at | DATETIME | |

### belts
| Column | Type | Notes |
|--------|------|-------|
| id | INT | Primary Key |
| color | VARCHAR(45) | e.g. yellow, red, black |
| created_at | DATETIME | |
| updated_at | DATETIME | |

### users_belts *(join table)*
| Column | Type | Notes |
|--------|------|-------|
| id | INT | Primary Key |
| users_id | INT | Foreign Key → users |
| belts_id | INT | Foreign Key → belts |
| created_at | DATETIME | when the belt was earned |

##  Relationships
- A **user** can earn many **belts** (many-to-many)
- A **belt** can be earned by many **users** (many-to-many)
- The `users_belts` table resolves the many-to-many relationship


## 🚀 How to Open Locally
1. Open MySQL Workbench
2. Go to **File → Open Model**
3. Select the `belt_erd.mwb` file
4. Click **Add Diagram** to view the ERD