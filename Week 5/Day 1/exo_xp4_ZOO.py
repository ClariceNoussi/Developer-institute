#ZOO
class Zoo():
    def __init__(self, zoo_name):
        self.animals=[]#liste vide dans crochets
        self.name=zoo.name

    def addAnimal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        
    def get_animal(self):
        for a in self.animals:
            print(a)
    def sort_animals(self, animal_sold):
        if animal_sold in self.animal:
            self.animal.remove(animal_sold)
    def sort_animal(self):
        for x in range (len(self.animals)): #ceci parcour les lettre du mots

        for y in range (len(self.animals)): #ceci parcourt les mot avec y allant de 0 a len(la longueur de la liste)
            #si s.a [x] s.a[y+1]
            #si sa[x], sa [y+2] ici on fait une comapariaison du prmier elet de la liste avec tous les elt de la liste et se concentrant uniquemant sur la premier lettre tel que defini par x