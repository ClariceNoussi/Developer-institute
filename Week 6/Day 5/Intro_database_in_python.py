import psycopg2
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Noussi4889+' #ici on peut garder notre mot de passe dans ne variable de sorte qu'une personne voulant utiliser hors de ma machine c'est impossible
DATABASE = 'dvdrental'
#connection object
c1=psycopg2.connect (host=HOSTNAME, user=USERNAME, password=PASSWORD , dbname=DATABASE) # here you put your pgsql password
cursor=c1.cursor()
#write queries
requete ="select *FROM customer Limit 10"

#Executes queries
cursor.execute(requete)

#get the results pf the select statement
resultats=cursor.fetchall()

print (resultats)