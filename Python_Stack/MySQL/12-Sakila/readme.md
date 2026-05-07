# MySQL Sakila Database - SQL Queries Assignment

This assignment demonstrates the use of SQL JOIN queries, filtering, and grouping on the `sakila` database.

---

## Queries

### 1. Customers inside city_id = 312
Returns the customer's first name, last name, email, address, and city.

### 2. All Comedy films
Returns the film title, description, release year, rating, special features, and genre.

### 3. All films joined by actor_id = 5
Returns the actor ID, full name, film title, description, and release year.

### 4. Customers in store_id = 1 inside cities (1, 42, 312, 459)
Returns the customer ID, first name, last name, email, and address.

### 5. Films with rating = G and special feature = Behind the Scenes joined by actor_id = 15
Returns the film title, description, release year, rating, and special features.

### 6. Actors joining film_id = 369
Returns the film ID, title, actor ID, and actor full name.

### 7. Drama films with rental rate = 2.99
Returns the film title, description, release year, rating, special features, and genre.

### 8. Action films joined by SANDRA KILMER
Returns the film title, description, release year, rating, special features, genre, and actor full name.

---

## How to Run
1. Open MySQL Workbench
2. Connect to your local MySQL server
3. Open the `.sql` file
4. Run `USE sakila;` first, then execute each query

---

## Technologies Used
- MySQL 9.7
- MySQL Workbench 8.0