import random # tjrs mettre les import en debut de programme
wordlist= ['girafe' ,'singe', 'chien', 'chat', 'grenouille']
mot_a_deviner= random.choice(wordlist)
tirets='- '*len(mot_a_deviner)

liste_tirets=tirets.split(' ') # pour avoir liste car input donnne tjrs string
tentatives=5

def input_letter():
    guessed_letter=input('enter la bonne lettre:')
    return guessed_letter


def verification(l):
    global tentatives #quand python estime que la variable a ete defini tres loin
    if l in mot_a_deviner:
        print('bravo')
        letter_index=mot_a_deviner.index(l)
        liste_tirets[letter_index]=l
        print(liste_tirets)
    elif l not in mot_a_deviner:
        print('wrong, try again')
        tentatives-=1
    print(liste_tirets)

def afficher():
    global tirets
    print(mot_a_deviner)
    while tentatives>0:
        letter=input_letter()
        verification(letter)
        tirets='-'.join(liste_tirets)# pour revenir a string
        print(tirets)
    if '_'not in tirets:
        print("winner")
        print ('end game')
break
        print('end game')
        
afficher()