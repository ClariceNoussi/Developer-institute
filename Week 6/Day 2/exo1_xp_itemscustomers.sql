--Tables of Public database 
CREATE TABLE items(
 items_id SERIAL PRIMARY KEY,
 desk_name VARCHAR NOT NULL,
 desk_price MONEY NOT NULL
)

CREATE TABLE customers(
 customers _id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL
)

--add items
INSERT INTO items (desk_name, desk_price) VALUES
('Small_desk', 100),
('Large_desk', 300),
('Fan', 80);

--add 5 customers
INSERT INTO custumers (first_name, last_name) VALUES
('Greg','Jones'),
('Sandra','Jones'),
('Scott','Scott'),
('Trevor','Green'),
('Melanie','Johnson');

--Use SQL to get the following from the database
--All items, ordered by price (lowest to highest)
SELECT * FROM items ORDER BY desk_price ASC;
--Items with a price above 80 (80 included), ordered by price (highest to lowest)
SELECT * FROM items WHERE desk_price >= '80' ORDER BY desk_price DESC;
--The first 3 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
SELECT last_name, first_name FROM custumers ORDER BY last_name, first_name ASC LIMIT 3;
--All last names (no other columns!), in reverse alphabetical order (Z-A)
SELECT last_name FROM custumers ORDER BY last_name DESC;

--Create a table named purchases. It should have 2 columns : customer_id and item_id
CREATE TABLE purchases(
    purchase_id SERIAL,
    PRIMARY KEY (purchase_id),
    FOREIGN KEY (items_id) REFERENCES (custumers_id)
);
--reponse a Does this work? Why/why not?=column "items_id" referenced in foreign key constraint does not exist

INSERT INTO purchases (movie_title, movie_story, actor_playing_id) VALUES




SELECT custumers.first_name, custumers.last_name from custumers  INNER JOIN desk_name.items, desk_price.items 
ON custumers_id.custumers=item_id.items


 