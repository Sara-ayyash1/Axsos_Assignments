-- 1. get the total revenue for March of 2012?
select MONTHNAME(charged_datetime) as Manth, sum(amount)  as total_revenue
from billing
where month(charged_datetime) =3 and year(charged_datetime) =2012;
-- --------------------------------------------------------------------
-- 2. get total revenue from the client with an id of 2?
SELECT client_id, SUM(amount) AS total_revenue
FROM billing
WHERE client_id = 2;
-- --------------------------------------------------------------------
-- 3. get all the sites a client with an ID of 10 owns?
select c.client_id , domain_name as website
from clients as c join sites as s
on c.client_id = s.client_id
where c.client_id =10;
-- --------------------------------------------------------------------
-- 4. get the total number of monthly sites created per year for the client with an ID of 1? What about the client with an ID of 20?
SELECT c.client_id, COUNT(s.site_id) AS number_of_websites, MONTHNAME(s.created_datetime) AS month_created, YEAR(s.created_datetime) AS year_created
FROM clients AS c 
JOIN sites AS s ON c.client_id = s.client_id
WHERE c.client_id = 1
GROUP BY year_created, month_created;

SELECT c.client_id, COUNT(s.site_id) AS number_of_websites, MONTHNAME(s.created_datetime) AS month_created, YEAR(s.created_datetime) AS year_created
FROM clients AS c 
JOIN sites AS s ON c.client_id = s.client_id
WHERE c.client_id = 20
GROUP BY year_created, month_created;
-- --------------------------------------------------------------------
-- 5. get the total # of leads generated for each site between January 1, 2011, and February 15, 2011?
SELECT s.site_id ,domain_name as website , count(l.leads_id) as total_of_leads
FROM leads as l join sites as s
on l.site_id = s.site_id
WHERE l.registered_datetime BETWEEN '2011-01-01' AND '2011-02-15'
group by s.site_id ;
-- --------------------------------------------------------------------
-- 6. get a list of client names and the total # of leads we've generated for each client between January 1, 2011, and December 31, 2011?
SELECT concat(c.first_name , " " , c.last_name) as client_name, count(l.leads_id) as total_of_leads
FROM leads as l join sites as s
on l.site_id = s.site_id
join clients as c on c.client_id = s.client_id
WHERE l.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
group by c.client_id;
-- --------------------------------------------------------------------
-- 7. get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?
SELECT concat(c.first_name , " " , c.last_name) as client_name, count(l.leads_id) as total_of_leads ,MONTHNAME(l.registered_datetime) AS month_generated
FROM leads as l join sites as s
on l.site_id = s.site_id
join clients as c on c.client_id = s.client_id
WHERE month(l.registered_datetime) BETWEEN 1 AND 6  and year(l.registered_datetime) = 2011
group by c.client_id , month(l.registered_datetime);
-- --------------------------------------------------------------------
-- 8. get a list of client names and the total # of leads we've generated for each client site between January 1, 2011, and December 31, 2011? 
-- Order this query by client ID.  
SELECT concat(c.first_name , " " , c.last_name) as client_name,domain_name as website, count(l.leads_id) as total_of_leads 
FROM leads as l join sites as s
on l.site_id = s.site_id
join clients as c on c.client_id = s.client_id
WHERE l.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
group by s.site_id
order by c.client_id;

-- Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.
SELECT concat(c.first_name , " " , c.last_name) as client_name, domain_name as website, count(l.leads_id) as total_of_leads 
FROM leads as l join sites as s
on l.site_id = s.site_id
right join clients as c on c.client_id = s.client_id
group by s.site_id
order by c.client_id;
-- --------------------------------------------------------------------
-- 9. Write single query that retrieves total revenue collected from each client for each month of the year.
-- Order by client ID.  First, this with, integer month, second with month name.  
SELECT concat(c.first_name , " " , c.last_name) as client_name, SUM(amount) AS total_revenue ,MONTH(charged_datetime) AS month_charged, YEAR(charged_datetime) AS year_charged
FROM billing as b join clients as c
on b.client_id = c.client_id
group by c.client_id , month_charged ,year_charged
order by c.client_id;

SELECT concat(c.first_name , " " , c.last_name) as client_name, SUM(amount) AS total_revenue ,monthname(charged_datetime) AS month_charged, YEAR(charged_datetime) AS year_charged
FROM billing as b join clients as c
on b.client_id = c.client_id
group by c.client_id , month_charged ,year_charged
order by c.client_id;
-- --------------------------------------------------------------------
-- 10. Write a singl  query th  retrieves all the sites that each client owns. Group the reslts so that each client's sites are displayed in a single field. 
-- It would be comwillebe if you add a new field called 'sites' with all the client's sites. (HINT  use  GRUP_CONCAT)
SELECT CONCAT(c.first_name, ' ', c.last_name) AS client_name, GROUP_CONCAT(s.domain_name SEPARATOR ' / ') AS sites
FROM clients AS c
left JOIN sites AS s ON c.client_id = s.client_id
GROUP BY c.client_id;