#with open('C:/Users/Clarice NOUSSI/Documents/Multiples projects/Developer Institute/Developers institute/Week 5/Day 4/nameslist.txt', 'r') as file:
    #for line in file.readlines(): # read the file line by line
     #   print(line)
    #fifth_caracter=file.readlines(5)#lecture des 5 premiers mots ou just print(file.readlines(5))
    #print(fifth_caracter)
    #print (file.read(3)) #lecture des 5 premiers caracters
    #entire_file=file.read()#lecture complet
    #list_name=entire_file.split('\n')# split pour passer de string a liste
    #print(list_name)
    #print(f'Darth apparait {list_name.count("Darth")} fois')#le nombre de fois qu'apparait un nom donnee
    #print(f'Luc apparait {list_name.count("Luc")} fois')
    #print(f'Lea apparait {list_name.count("Lea")} fois')

#pour ajouter son nom a la fin, on utlise a, si on utilise w, ca efface tout pour mettre le nouveau texte
with open('C:/Users/Clarice NOUSSI/Documents/Multiples projects/Developer Institute/Developers institute/Week 5/Day 4/nameslist.txt', 'a') as file:
    file.write('\n Clarice')
    # ajouter Skywalker devant luke a chaque fois

with open('C:/Users/Clarice NOUSSI/Documents/Multiples projects/Developer Institute/Developers institute/Week 5/Day 4/nameslist.txt', 'r+') as file:
    for line in file.readlines():
      
        if 'Luke' in line:
            file.write('Skywalker')# a revoir
            