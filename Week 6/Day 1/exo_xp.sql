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

--fetch all the items= run
--fetch items with price<80$
SELECT * FROM items WHERE desk_price > 80
--items avec prix au dela de 300
SELECT * FROM items WHERE desk_price <= 300
--customers with last name smith: result=empty table
SELECT * FROM custumers WHERE first_name LIKE 'Smith';
--customers with last name Scott
SELECT * FROM custumers WHERE first_name LIKE 'Scott';
--customers whose firstname is not ‘Scott’
SELECT * FROM custumers WHERE first_name !='Scott';
