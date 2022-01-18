import random

wordlist=['girafe','singe','chien', 'chat', 'grenouille']

mot_a_deviner = random.choice(wordlist)
print(mot_a_deviner)

tirets = '_ '*len(mot_a_deviner)
liste_tirets = tirets.split(' ')
print(tirets)
tentatives = 5


def input_letter():
	guessed_letter = input('Entrer la bonne lettre :')
	return guessed_letter


def verification(l):
	global tentatives
	if l in mot_a_deviner: 
		print('Bravo')
		letter_index = mot_a_deviner.index(l)
		liste_tirets[letter_index] = l
		print(liste_tirets)
	else:
		print('wrong letter')
		tentatives-=1
	

def afficher():
	
	while tentatives > 0 :
		letter = input_letter()
		verification(letter)
		tirets = ' '.join(liste_tirets)
		print(tirets)
		if '_' not in liste_tirets:
			print('Bravo tu as trouvé le mot')
			break
	print('End of game')

afficher()