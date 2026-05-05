# Product Categories ERD

##  Description
Entity Relationship Diagram for a product browsing system built with MySQL Workbench. The goal was to analyze a UI wireframe showing products organized by categories and subcategories, then transform it into a structured database schema.

##  Wireframe Analysis
The wireframe shows products that can be browsed by **Brand**, **Category**, and **Character**. Under each category (e.g. *Action Figures*), there are multiple subcategories (e.g. *Accessories*, *Military Figures*, *Animals*...).

This revealed two key insights:
1. **Categories can contain other categories** → a category needs a `parent_id` referencing itself (self-referencing relationship).
2. **A product can belong to multiple categories, and a category can have multiple products** → a many-to-many relationship requiring a join table.

##  Key Concepts
- **Self-Referencing Relationship:** The `categories` table references itself using `parent_id` to represent parent/child categories. If `parent_id` is NULL, the category is a top-level parent.
- **Many-to-Many Relationship:** A product can belong to multiple categories and a category can have multiple products, handled via the `category_products` join table.
- **Normalization:** Data is separated into focused tables to avoid redundancy.
- **Temporal Tracking:** `created_at` and `updated_at` timestamps are included for historical tracking.

##  Tables

### categories
| Column | Type | Notes |
|--------|------|-------|
| id | INT | Primary Key |
| name | VARCHAR(45) | |
| created_at | DATETIME | |
| updated_at | DATETIME | |
| parent_id | INT | Foreign Key → categories (self-reference) |

### products
| Column | Type | Notes |
|--------|------|-------|
| id | INT | Primary Key |
| name | VARCHAR(45) | |
| price | DECIMAL(15,2) | |

### category_products *(join table)*
| Column | Type | Notes |
|--------|------|-------|
| id | INT | Primary Key |
| products_id | INT | Foreign Key → products |
| categories_id | INT | Foreign Key → categories |

##  Relationships
- A **category** can have many **subcategories** (self-referencing one-to-many)
- A **product** can belong to many **categories** (many-to-many)
- A **category** can have many **products** (many-to-many)
- The `category_products` table resolves the many-to-many relationship

##  How to Open Locally
1. Open MySQL Workbench
2. Go to **File → Open Model**
3. Select the `.mwb` file
4. Click **Add Diagram** to view the ERD
