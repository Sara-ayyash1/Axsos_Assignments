# SQL Assignment: Lead Gen Business 

## Overview

This assignment practices writing SQL queries using the **lead-gen-business-new** database. It covers `JOIN`, `GROUP BY`, `BETWEEN`, date functions, aggregate functions, and `GROUP_CONCAT`.

---

## Database Schema

| Table     | Key Fields                                                                 |
|-----------|----------------------------------------------------------------------------|
| `billing` | `billing_id`, `amount`, `charged_datetime`, `client_id`                   |
| `clients` | `client_id`, `first_name`, `last_name`, `email`, `joined_datetime`        |
| `leads`   | `leads_id`, `first_name`, `last_name`, `registered_datetime`, `email`, `site_id` |
| `sites`   | `site_id`, `domain_name`, `created_datetime`, `client_id`                 |

---

## Queries

### 1. Total Revenue for March 2012

```sql
SELECT MONTHNAME(charged_datetime) AS Month, SUM(amount) AS total_revenue
FROM billing
WHERE MONTH(charged_datetime) = 3 AND YEAR(charged_datetime) = 2012;
```

---

### 2. Total Revenue from Client ID 2

```sql
SELECT client_id, SUM(amount) AS total_revenue
FROM billing
WHERE client_id = 2;
```

---

### 3. All Sites Owned by Client ID 10

```sql
SELECT c.client_id, domain_name AS website
FROM clients AS c
JOIN sites AS s ON c.client_id = s.client_id
WHERE c.client_id = 10;
```

---

### 4. Monthly Sites Created Per Year — Client ID 1 & 20

```sql
-- Client ID 1
SELECT c.client_id, COUNT(s.site_id) AS number_of_websites,
       MONTHNAME(s.created_datetime) AS month_created,
       YEAR(s.created_datetime) AS year_created
FROM clients AS c
JOIN sites AS s ON c.client_id = s.client_id
WHERE c.client_id = 1
GROUP BY year_created, month_created;

-- Client ID 20
SELECT c.client_id, COUNT(s.site_id) AS number_of_websites,
       MONTHNAME(s.created_datetime) AS month_created,
       YEAR(s.created_datetime) AS year_created
FROM clients AS c
JOIN sites AS s ON c.client_id = s.client_id
WHERE c.client_id = 20
GROUP BY year_created, month_created;
```

---

### 5. Total Leads Per Site — Jan 1 to Feb 15, 2011

```sql
SELECT s.site_id, domain_name AS website, COUNT(l.leads_id) AS total_of_leads
FROM leads AS l
JOIN sites AS s ON l.site_id = s.site_id
WHERE l.registered_datetime BETWEEN '2011-01-01' AND '2011-02-15'
GROUP BY s.site_id;
```

---

### 6. Total Leads Per Client — Full Year 2011

```sql
SELECT CONCAT(c.first_name, ' ', c.last_name) AS client_name,
       COUNT(l.leads_id) AS total_of_leads
FROM leads AS l
JOIN sites AS s ON l.site_id = s.site_id
JOIN clients AS c ON c.client_id = s.client_id
WHERE l.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY c.client_id;
```

---

### 7. Total Leads Per Client Per Month — Jan to Jun 2011

```sql
SELECT CONCAT(c.first_name, ' ', c.last_name) AS client_name,
       COUNT(l.leads_id) AS total_of_leads,
       MONTHNAME(l.registered_datetime) AS month_generated
FROM leads AS l
JOIN sites AS s ON l.site_id = s.site_id
JOIN clients AS c ON c.client_id = s.client_id
WHERE MONTH(l.registered_datetime) BETWEEN 1 AND 6
  AND YEAR(l.registered_datetime) = 2011
GROUP BY c.client_id, MONTH(l.registered_datetime);
```

---

### 8. Total Leads Per Client Site — 2011, Ordered by Client ID

```sql
-- By date range
SELECT CONCAT(c.first_name, ' ', c.last_name) AS client_name,
       domain_name AS website,
       COUNT(l.leads_id) AS total_of_leads
FROM leads AS l
JOIN sites AS s ON l.site_id = s.site_id
JOIN clients AS c ON c.client_id = s.client_id
WHERE l.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY s.site_id
ORDER BY c.client_id;

-- All time (includes clients with no leads via RIGHT JOIN)
SELECT CONCAT(c.first_name, ' ', c.last_name) AS client_name,
       domain_name AS website,
       COUNT(l.leads_id) AS total_of_leads
FROM leads AS l
JOIN sites AS s ON l.site_id = s.site_id
RIGHT JOIN clients AS c ON c.client_id = s.client_id
GROUP BY s.site_id
ORDER BY c.client_id;
```

---

### 9. Total Revenue Per Client Per Month — Integer & Month Name

```sql
-- With integer month
SELECT CONCAT(c.first_name, ' ', c.last_name) AS client_name,
       SUM(amount) AS total_revenue,
       MONTH(charged_datetime) AS month_charged,
       YEAR(charged_datetime) AS year_charged
FROM billing AS b
JOIN clients AS c ON b.client_id = c.client_id
GROUP BY c.client_id, month_charged, year_charged
ORDER BY c.client_id;

-- With month name
SELECT CONCAT(c.first_name, ' ', c.last_name) AS client_name,
       SUM(amount) AS total_revenue,
       MONTHNAME(charged_datetime) AS month_charged,
       YEAR(charged_datetime) AS year_charged
FROM billing AS b
JOIN clients AS c ON b.client_id = c.client_id
GROUP BY c.client_id, month_charged, year_charged
ORDER BY c.client_id;
```

---

### 10. All Sites Per Client Using GROUP_CONCAT

```sql
SELECT CONCAT(c.first_name, ' ', c.last_name) AS client_name,
       GROUP_CONCAT(s.domain_name SEPARATOR ' / ') AS sites
FROM clients AS c
LEFT JOIN sites AS s ON c.client_id = s.client_id
GROUP BY c.client_id;
```

---

## Key Concepts Used

| Concept | Description |
|---|---|
| `JOIN` | Combines rows from multiple tables based on related columns |
| `LEFT JOIN` / `RIGHT JOIN` | Includes rows even when there's no match in the other table |
| `GROUP BY` | Groups rows to apply aggregate functions |
| `BETWEEN` | Filters rows within a date or value range |
| `MONTH()` / `YEAR()` / `MONTHNAME()` | Extracts date parts for filtering and display |
| `SUM()` / `COUNT()` | Aggregate functions for totals |
| `CONCAT()` | Combines strings (e.g. first + last name) |
| `GROUP_CONCAT()` | Concatenates grouped values into a single string |