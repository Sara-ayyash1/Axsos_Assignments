# Yelp - Food Reviews ERD

##  Description
Entity Relationship Diagram for a Yelp-like food review application built with MySQL Workbench. The goal was to analyze a UI wireframe and transform it into a structured database schema with proper relationships between Users, Restaurants, and Reviews.

##  Key Concepts
- **Requirement Analysis:** Identifying core entities from the wireframe (Users, Restaurants, Reviews).
- **One-to-Many Relationships:** A user can write many reviews, and a restaurant can have many reviews.
- **Normalization:** Data is distributed across tables to avoid redundancy.
- **Naming Conventions:** Using clear and consistent column names with foreign keys referencing their parent tables.

##  Tables

### users
| Column | Type | Notes |
|--------|------|-------|
| user_id | INT | Primary Key |
| first_name | VARCHAR(100) | |
| last_name | VARCHAR(100) | |
| email | VARCHAR(500) | |
| img_profile | VARCHAR(500) | |

### restaurants
| Column | Type | Notes |
|--------|------|-------|
| restaurant_id | INT | Primary Key |
| name | VARCHAR(100) | |
| address | VARCHAR(300) | |
| photo_url | VARCHAR(500) | |

### reviews
| Column | Type | Notes |
|--------|------|-------|
| review_id | INT | Primary Key |
| rating | INT | |
| content | TEXT | |
| created_at | DATETIME | |
| user_id | INT | Foreign Key → users |
| restaurant_id | INT | Foreign Key → restaurants |

##  Relationships
- A **user** can write many **reviews** (one-to-many)
- A **restaurant** can have many **reviews** (one-to-many)
- A **review** belongs to one user and one restaurant

##  How to Open Locally

1. Download MySQL Workbench from [mysql.com/products/workbench](https://www.mysql.com/products/workbench/) ```
2. Open MySQL Workbench
3. Go to **File → Open Model**
4. Select the `Food_Reviews_ERD.mwb` file
5. Click **Add Diagram** to view the ERD