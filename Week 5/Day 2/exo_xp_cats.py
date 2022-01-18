class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
# DEBUT NOTRE CODE
# qst 1 
class Cat1(Cat):
    pass

 #qst 2   
Cat1=Cat ('minou',2)
Cat2=Cat ('mina',3)
Cat3=Cat ('toutou',5 )

#qst 3
my_cats=[Cat1, Cat2, Cat3]

#qst 4
My_pets=my_cats
#qst 5
My_pets.walk()



