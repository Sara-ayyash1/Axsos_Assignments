use sakila;
-- -------------------------------------------------------------------
/*1. get all the customers inside city_id = 312
Your query should return the customer's first name, last name, email, and address.*/

select ci.city_id ,first_name , last_name , email ,a.address ,ci.city
from customer as c join address as a 
on c.address_id = a.address_id
join city ci
on a.city_id = ci.city_id
where ci.city_id = 312;

-- -------------------------------------------------------------------
/*2. get all comedy films, Your query should return the film title, description, release year, rating, special features, and genre (category).*/

select f.film_id ,title , description , release_year , rating ,special_features ,name as genre
from film as f join film_category as fc
on f.film_id = fc.film_id
join category as c
on fc.category_id = c.category_id
where name = 'Comedy';
-- -------------------------------------------------------------------
/*3. get all the films joined by actor_id=5, Your query should return the actor ID, name, film title, description, and release year.*/

select a.actor_id , concat(first_name ," ", last_name) as name ,title , description ,release_year
from film as f join film_actor as fa
on f.film_id = fa.film_id
join actor as a
on fa.actor_id = a.actor_id
where a.actor_id=5;
-- -------------------------------------------------------------------
/*4. get all the customers in store_id = 1 and inside these cities (1, 42, 312, and 459),
Your query should return the customer's first name, last name, email, and address.*/
select customer_id , first_name , last_name , email ,address
from customer  as c join address as a 
on c.address_id = a.address_id
join city as ci 
on a.city_id = ci.city_id
where store_id =1 and ci.city_id in(1, 42, 312, 459);

-- -------------------------------------------------------------------
/*5. get all the films with a "rating = G" and "special feature = behind the scenes",joined by actor_id = 15, 
Your query should return the film title, description, release year, rating, and special feature. 
Hint: You may use the LIKE function to get the 'behind the scenes' part.*/

select f.film_id , title, description, release_year, rating ,special_features, actor_id  
from film as f join film_actor as fa
on f.film_id = fa.film_id
where rating  ='G' and  actor_id = 15 and special_features LIKE('%behind the scenes%');
-- -------------------------------------------------------------------
/*6. get all the actors joining the film_id = 369, Your query should return the film_id, title, actor_id, and actor_name.*/

select f.film_id , title, a.actor_id , concat(first_name ," ", last_name) as name 
from film as f join film_actor as fa
on f.film_id = fa.film_id
join actor as a
on fa.actor_id = a.actor_id
where f.film_id  =369;
-- -------------------------------------------------------------------
/*7. get all drama films with a rental rate of 2.99, Your query should return the film title, 
description, release year, rating, special features, and genre (category).*/

select f.film_id ,title , description , release_year , rating ,special_features ,name as genre
from film as f join film_category as fc
on f.film_id = fc.film_id
join category as c
on fc.category_id = c.category_id
where name = 'drama' and rental_rate = 2.99;
-- -------------------------------------------------------------------
/*8. get all the action films joined by SANDRA KILMER, Your query should return the film title, 
description, release year, rating, special features, genre (category), and actor's first and last name.*/

select f.film_id ,title , description , release_year , rating ,special_features ,name as genre , concat(first_name ," ", last_name) as actor_name 
from film as f join film_category as fc
on f.film_id = fc.film_id
join category as c on fc.category_id = c.category_id
join film_actor as fa on f.film_id = fa.film_id
join actor as a on fa.actor_id = a.actor_id
where name = 'action' and  CONCAT(first_name, " ", last_name) = 'SANDRA KILMER';