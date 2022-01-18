#exercise 1"
#Question 1 et 2
def my_function():
    number=input('Entrez un nombre negatif')
    chiffre=int(number)
    print(chiffre) #I start with integer because an input always returns a string and the rest of built function is apply on number
    print(abs(chiffre))
    print(number)
    print(my_function.__doc__)

my_function()

"""exercise xp 2"""
'''donnees d'entreee est une liste :c1, c2,c3,c4 contenant currency and amount 
output:amount and currency pour chaque c en string, ce qui suppose une liste au depart, 
int pour transformer le string precedent en nombre
repr qui signifie representation qui rtourne un objet
 '''

C1=("dollars",5)
C2=("dollars",10)
C3=("shekel",1)
C4=("shekel",10)
print(f'currency {C1}')
print(f'currency {C2}')
print(f'currency {C3}')
print(f'currency {C4}')
string_C1=C1[1]
print(string_C1)
Amount_C1=int(string_C1)
print (Amount_C1)
objet_initial=repr(Amount_C1)
print(objet_initial)
print((Amount_C1)+5) #avec string_c1 on n'a pas de resultat bien que ce soit un chiffre donc c'est un string

#c1+c2
string_C2=C2[1]
Amount_C2=int(string_C2)
print(Amount_C1+Amount_C2)

print(Amount_C1)

Amount_C1 +=5
print(Amount_C1)

Amount_C1 += Amount_C2
print (Amount_C1)

#print(C1+C3) ca donne un tuple avec les 4 parametres a l'interieur des parentheses
if C1+C3:
    raise Exception ('Cannot add between Currency type <dollar> and <shekel>-3') 


