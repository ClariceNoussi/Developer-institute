from typing import ItemsView
import psycopg2
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Noussi4889+' #ici on peut garder notre mot de passe dans ne variable de sorte qu'une personne voulant utiliser hors de ma machine c'est impossible
DATABASE = 'MenuItem'
c1=psycopg2.connect (host=HOSTNAME, user=USERNAME, password=PASSWORD , dbname=DATABASE) # here you put your pgsql password
cursor=c1.cursor()
#write queries
requete ="select *FROM customer Limit 10"

#Executes queries
cursor.execute(requete)

#get the results pf the select statement
resultats=cursor.fetchall()

class MenuItem():
    def __init__(self, name, price):
        self.name=name
        self.price=price
    
    def save(self):
        query ="INSERT INTO MenuItem(name, price) VALUES('{self.name}', {self.price});"
        return query

    def delete(self):
       query="DELETE FROM Menuitem WHERE '(name = '{self.name})'' and (price={self.price})"
       return query
    def update(self):
        query='UPDATE MenuItems WHERE "(name ={self.name})"  and "(price={self.price})"'
        return query 
    def All(self):
        query= "Select*from MenuItem;"
        return query
    def get_the_name(self, n):
        query='Select name from MenuItem where name="{n}"'
        cursor.execute(query)
        results=cursor.fetchall():
        print(results)


        


cur.close



    
item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)
item2 = MenuItem.get_by_name('Beef Stew')
items = MenuItem.all()
