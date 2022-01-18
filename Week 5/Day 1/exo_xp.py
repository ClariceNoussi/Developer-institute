from typing import AsyncGenerator


class Cats():
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print (f'the cat name is {self.name} and he is {self.age}')

#instantiate 3 Cats
C1=Cats('minette', 2)
C2=Cats('roky', 1)
C3=Cats('miaou', 3)

def oldest_cat():
    #if C1.age > C2.age and C3.age > C1.age and C2.age > C3.age:
     #   print(f'the oldest cat is {C1.name} and he is {C1.age}')
    max(1,2,3) 
        print(f'the oldest cat is {C1.name} and he is {C1.age}')
oldest_cat()