# Books - Favorite Books ERD

## Requirements Analysis
- Each **book** has a title and an author name
- Each **user** can save a list of their favorite books
- A user can have many favorite books, and a book can be favorited by many users → **many-to-many relationship**

> Note: The author's name is stored directly in the `books` table as `author_name` (as specified in the assignment). A separate `authors` table would be better normalized but is out of scope here.

##  Key Concepts
- **Many-to-Many Relationship:** A user can favorite many books, and a book can be favorited by many users — resolved using the `favorite` join table.
- **Join Table:** The `favorite` table holds only the two foreign keys (`users_user_id`, `books_book_id`) to link users and books.
- **Normalization Note:** Author data is denormalized into the `books` table intentionally per assignment requirements.

##  Tables

### users
| Column | Type | Notes |
|--------|------|-------|
| user_id | INT | Primary Key |
| name | VARCHAR(45) | |

### books
| Column | Type | Notes |
|--------|------|-------|
| book_id | INT | Primary Key |
| title | VARCHAR(45) | |
| author_name | VARCHAR(45) | |

### favorite *(join table)*
| Column | Type | Notes |
|--------|------|-------|
| id | INT | Primary Key |
| users_user_id | INT | Foreign Key → users |
| books_book_id | INT | Foreign Key → books |

##  Relationships
- A **user** can favorite many **books** (many-to-many)
- A **book** can be favorited by many **users** (many-to-many)
- The `favorite` table resolves the many-to-many relationship


##  How to Open Locally
1. Open MySQL Workbench
2. Go to **File → Open Model**
3. Select the `.mwb` file
4. Click **Add Diagram** to view the ERD