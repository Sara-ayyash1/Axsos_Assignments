# Yelp - Food Reviews ERD

## Description
Entity Relationship Diagram for a Yelp-like food review application built with MySQL Workbench.

## Tables

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
| restaurant_ID | INT | Primary Key |
| name | VARCHAR(100) | |
| adress | VARCHAR(300) | |
| photo_url | VARCHAR(500) | |

### reviews
| Column | Type | Notes |
|--------|------|-------|
| review_id | INT | Primary Key |
| rating | INT | |
| content | TEXT | |
| created_at | DATETIME | |
| user_id | INT | Foreign Key → users |
| restaurants_restaurant_ID | INT | Foreign Key → restaurants |

## How to Open Locally

1. Download MySQL Workbench from [mysql.com/products/workbench](https://www.mysql.com/products/workbench/)
2. Clone this repo
   ```
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   ```
3. Open MySQL Workbench
4. Go to **File → Open Model**
5. Select the `Food_Reviews_ERD.mwb` file
6. Click **Add Diagram** to view the ERD

## Relationships
- A **user** can write many **reviews** (one-to-many)
- A **restaurant** can have many **reviews** (one-to-many)
- A **review** belongs to one user and one restaurant