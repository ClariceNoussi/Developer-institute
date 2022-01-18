--Bootcamp
CREATE TABLE actors(
 student_id SERIAL PRIMARY KEY,
 last_name VARCHAR (50) NOT NULL,
 first_name VARCHAR (100) NOT NULL,
 birth_date DATE NOT NULL;
)
--avaerage numbers of oscar
SELECT avg(number_oscars) AS average_number_oscars FROM actors;
