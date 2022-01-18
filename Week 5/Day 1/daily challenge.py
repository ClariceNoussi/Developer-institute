class Farm:
    def __init__(self, name):
            self.name=name
            self.animals={}
    def Add_animal(self, animal_name, number_animal=1) # on utilise == quand on fait une comparaison
        self.animals.update({animal_name:number_animal}) #pour ajouter un elt dans un dictionaire
        if animal_name in self.animals:
            self.animals[animal_name]+=number_animal  #pour donner une nouvelle valeur a notre cle c'est dic_name[cle]=new_value
        else:
            self.animals.update({animal_name:number})
    def Get_info(Self):
        print(f'{self.name}')
        for(key,value) in self.animals.items():
            print (f'{key}:{value}')

Get_info()


    