CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
)

--add 2 female actors one by one
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Oprah','winfrey','29/01/1954', 3);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Joanne','Rowling','31/07/1965', 1);

--add 3 mor actors
INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES
('Merv','Griffin','31/07/1925', 4),
('Shahrukh','Kan','02/10/1965', 8),
('Tom','Cruise','03/07/1965', 5;

--retrieve the first 4 actors
SELECT * FROM actors LIMIT 4;
--4 authors in ascending order
SELECT * FROM actors ORDER BY last_name ASC
--The actors that have the letter 'e' in their first_name
SELECT * FROM actors WHERE first_name LIKE '%e%';
--The actors that got at least 5 oscars
SELECT * FROM Actors WHERE number_oscars >=5;
--count how many actors in the table
SELECT count(Actor_id) FROM Actors;
--Add actor with some blanks fields, what to you think the outcome will be
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('new actor','','04/10/1920', 1);
--the above works,but if first name, last name and numbers of awards are absents, we will have a message Error'invalid input synthax