# Normalization - Student & Dojo ERD

## Original Problems

### Original ERD had:
| Problem | Violation |
|--------|-----------|
| `interests TEXT` storing multiple values (e.g. "coding, gaming") | 1NF |
| `address1` and `address2` as repeating columns | 1NF |
| `dojo_id` in students assuming one dojo per student | Many-to-Many ignored |

##  Normalization Steps

### 1NF — First Normal Form
**Rule:** Every column must hold a single atomic value. No repeating columns.

- ❌ `interests` stored multiple values in one cell → ✅ moved to a separate `interests` table
- ❌ `address1` and `address2` were repeating columns → ✅ moved to a separate `addresses` table

### 2NF — Second Normal Form
**Rule:** Every non-key column must depend on the entire primary key.

- ✅ After splitting into separate tables, all columns depend fully on their table's primary key

### 3NF — Third Normal Form
**Rule:** No column should depend on another non-key column (no transitive dependency).

- ✅ `location` stays in `dojos` table, not in `students` — so it depends on `dojo_id`, not `student_id`
- ✅ No transitive dependencies remain after restructuring

##  Final Tables

### dojos
| Column | Type | Notes |
|--------|------|-------|
| id | INT | Primary Key |
| name | VARCHAR(255) | |
| location | VARCHAR(255) | |
| created_at | DATETIME | |
| updated_at | DATETIME | |

### students
| Column | Type | Notes |
|--------|------|-------|
| id | INT | Primary Key |
| name | VARCHAR(255) | |
| created_at | DATETIME | |
| updated_at | DATETIME | |

### addresses
| Column | Type | Notes |
|--------|------|-------|
| id | INT | Primary Key |
| student_id | INT | Foreign Key → students |
| address | VARCHAR(255) | |

### interests
| Column | Type | Notes |
|--------|------|-------|
| id | INT | Primary Key |
| student_id | INT | Foreign Key → students |
| interest | VARCHAR(255) | |

##  Relationships
- A **dojo** can have many **students**, and a **student** can belong to one **dojos** 
- A **student** can have many **addresses** (one-to-many)
- A **student** can have many **interests** (one-to-many)


##  How to Open Locally
1. Open MySQL Workbench
2. Go to **File → Open Model**
3. Select the `.mwb` file
4. Click **Add Diagram** to view the ERD