#exo xp n2
class Currency():
    def ___init__(self, type, amount):
        self.type=type
        self.amount=amount
    def __str__(self):
        return f'{self.amount} {self.type}'
    def __int(self):
        return self.amount
    def __repr__(self)
        return f'{self.amount} {self.type}s'
    def __add__(self, n): #cette dunder method permet d'additionner 2 objet car repr donne les objets
        if self.type == type:
            return int(self)+int(self.amount)
        else:
            return TypeError('Cannot add between Currency type {self.type} and {other.type}>')

    def __iadd__(self, n)# iadd est la dunder method correspondant a +=  a finir
        return

C1=("dollars",5)
C2=("dollars",10)
C3=("shekel",1)
C4=("shekel",10)