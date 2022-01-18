--1.In the dvdrental database write a query to select all the columns from the “customer” table.
select*from customer;
--2.Write a query to display the names (first_name, last_name) using an alias named “full_name”.
SELECT (first_name||''|| last_name) AS full_name FROM customer;
--3.Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).
select all the create_date from customer;
--4.Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.
SELECT first_name FROM customer ORDER BY first_name DESC with distinct on first;
--5.Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;
--6.Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.
SELECT address_id, phone FROM address WHERE address='Texas'; --zero resultat
--7.Write a query to retrieve all movie details where the movie id is either 15 or 150.
SELECT *FROM film WHERE film_id=15 or film_id=150;
--8.Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.
Select film_id, title, description, lengtH, rental_rate FROM film where title='Titanic';
--9.No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
Select film_id, title, description, lengtH, rental_rate FROM film WHERE title LIKE 'Ti%';
--10.Write a query which will find the 10 cheapest movies.
SELECT * FROM film ORDER BY rental_rate Asc limit 10;
--11.Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
SELECT* FROM film ORDER BY rental_rate Asc OFFSET 10 FETCH FIRST 10 ROW ONLY;
--12.Write a query which will join the data in the customer table and the payment table. You want to get the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
SELECT amount, payment_date, customer.customer_id FROM payment INNER JOIN customer
ON payment.customer_id = customer.customer_id order by customer.customer_id ASC;
--13. (reponse left join)You need to check your inventory. Write a query to get all the movies which are not in inventory (l'enfeant  ici c'est invntory c'est lui aui contient film_id).
select title from film left join inventory on film.film_id=inventory.film_id 
--14.Write a query to find which city is in which country.
select city.city, country.countru from city inner join country
on customer.customer_idp=ayment.customer_id
--15.(2 join car 3 tables)Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.
Select customer.first_name, payment_amount, staff.first_name as seller from customer 
inner join payment on customer.customer_id=payment.customer _id
inner join staff on payment.staff_id=staff.staff_id;
--bonus2: quel customer a achete combien de film avec prenom
select customer.first_name, count(amount) from payment inner join customer  
on payment.customer_id=customer_id group by customer.first_name;
--nombre de vendeurs
Select first_name from staff;
--nombre de vente de chacun
select first_name, count(payment.staff_id) from staff inner join payment on
staff.staff_id = payment.staff_id group by first_name;
--combien d'acteurs jouent dans chaque film
select film_title, count(actor_id.actor_id) from film
join film_actor.film on film_actor.film_id=film_id group by first name
--dans combien de film a joue chaque acteur (avant dernier dans slack)
select actor.first_name, count(film_actor.film_id) as nombre_de_films from actor join film_actor
on film_actor.actor_id = actor.actor_id group by actor.first_name;
--qui a tourne dans plus de film
select actor.first_name, count(film_actor.film_id) as nombre_de_films from actor join film_actor
on film_actor.actor_id = actor.actor_id group by actor.first_name order by count(film_actor.film_id) desc limit 1;