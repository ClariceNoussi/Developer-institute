#ecrire un programme qui demande d'ecrire un mot et de definir le nombre de voyelle
mot=input('entrer votre mot correct')
List_voyelle=['a', 'e', 'i', 'o', 'u', 'y']
def nombre_voyelle():
    count=0
    for n in mot:
        if n in List_voyelle:
            n.count+=1
            print(n.count)

nombre_voyelle()