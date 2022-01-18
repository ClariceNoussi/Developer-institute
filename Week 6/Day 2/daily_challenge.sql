CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')

SELECT * FROM FirstTab

CREATE TABLE SecondTab (
    id integer 
)

INSERT INTO SecondTab VALUES
(5),
(NULL)


SELECT * FROM SecondTab
--DATA
--Table1 – FirstTab
ID  Name
5   Pawan
6   Sharlee
7   Krish
NULL    Avtaar


--Table2 – SecondTab
ID
5
NULL
--Q1. What will be the OUTPUT of the following statement?\
SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL ) --une comparaison avec Null comme le resultat de la partie entre parenthese nous renvois le null
--on utilise 'Not in' generalement pour une liste

--Q2. What will be the OUTPUT of the following statement?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
    --ici on aura 2 car on compte le nombre d'element de la liste ici c'est 6 et 7 , 5 est exclu avec la condition entre parenthese 

Q3. What will be the OUTPUT of the following statement?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
--2 egalement pour 6 et 7 car on a exclu 5 et null avec la partie entre parenthese
--Q4. What will be the OUTPUT of the following statement?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL
    --result 2 egalement car 5 exclu avec la condition entre parenthese et on ne compte pas le null