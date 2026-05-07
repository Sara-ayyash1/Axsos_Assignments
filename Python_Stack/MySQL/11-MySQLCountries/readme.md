# MySQL World Database 
This assignment demonstrates the use of SQL JOIN queries, filtering, grouping, and ordering on the `world` database.

---

## Queries

### 1. Countries that speak Slovene
Returns the country name, language, and percentage, ordered by language percentage in descending order.

### 2. Total number of cities per country
Returns each country's name and total number of cities, ordered by the number of cities in descending order.

### 3. Cities in Mexico with population greater than 500,000
Returns city names and population in Mexico, ordered by population in descending order.

### 4. Languages with percentage greater than 89%
Returns all languages spoken in each country with a percentage greater than 89%, ordered by percentage in descending order.

### 5. Countries with Surface Area below 501 and Population greater than 100,000
Returns country name, surface area, and population.

### 6. Constitutional Monarchies with capital > 200 and life expectancy > 75
Returns country name, government form, capital, and life expectancy.

### 7. Cities in Argentina's Buenos Aires district with population > 500,000
Returns country name, city name, district, and population.

### 8. Number of countries per region
Returns each region and the number of countries in it, ordered by count in descending order.

---

## How to Run
1. Open MySQL Workbench
2. Connect to your local MySQL server
3. Open the `queries.sql` file
4. Run `USE world;` first, then execute each query

---

## Technologies Used
- MySQL 9.7
- MySQL Workbench 8.0