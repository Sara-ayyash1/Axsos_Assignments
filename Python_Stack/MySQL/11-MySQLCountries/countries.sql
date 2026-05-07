use world;
-- ------------------------------------------------------
/*1. get all the countries that speak Slovene? 
Your query should return the name of the country, language, and language percentage. 
Your query should arrange the result by language percentage in descending order*/

SELECT name , language , percentage
FROM countries as c join languages as l 
on c.id = l.country_id
where language = 'Slovene'
order by percentage desc;
-- ------------------------------------------------------
/*2.display each country's total number of cities?
Your query should return the name of the country and the total number of cities.
Your query should arrange the result by the number of cities in descending order*/

select co.name ,count(ci.id) as number_of_cities
from countries as co join cities as ci
on co.id = ci.country_id
group by co.id
order by number_of_cities desc;
-- ------------------------------------------------------
/*3. get all the cities in Mexico with a population greater than 500,000?
 Your query should arrange the results by population in descending order*/
 
select co.id ,ci.name  ,ci.population
from countries as co join cities as ci
on co.id = ci.country_id
where co.name = 'Mexico' and ci.population > 500000
order by ci.population desc;
-- ------------------------------------------------------
/*4. get all languages in each country with a percentage greater than 89% ?
Your query should arrange the result by percentage in descending order.*/

SELECT name , language , percentage
FROM countries as c join languages as l 
on c.id = l.country_id
where percentage > 89.00
order by percentage desc;
-- ------------------------------------------------------
/*5. get all the countries with a Surface Area below 501 and a Population greater than 100,000?*/

select name , surface_area , population 
from countries
where surface_area< 501 and population > 100000; 
-- ------------------------------------------------------
/*6. get countries with only a Constitutional Monarchy with a 
capital greater than 200 and a life expectancy greater than 75 years?*/

select name , government_form , capital  , life_expectancy
from countries
where government_form = 'Constitutional Monarchy' and capital > 200 and life_expectancy > 75 ;
-- ------------------------------------------------------
/*7.get all the cities of Argentina inside the Buenos Aires district and have a population greater than 500,000? 
The query should return the Country Name, City Name, District, and Population.*/

select co.name ,ci.name , district , ci.population 
from countries as co join cities as ci
on co.id = ci.country_id
where co.name = 'Argentina' and district = 'Buenos Aires' and ci.population > 500000;

-- ------------------------------------------------------
/*8. summarize the number of countries in each region? 
The query should display the region's name and the number of countries. 
Also, the query should arrange the result by the number of countries in descending order*/

select region  , count(id) as countries
from countries
group by region
order by countries desc;
