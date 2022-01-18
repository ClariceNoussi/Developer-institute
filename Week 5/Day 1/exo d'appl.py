
class Robot():
   def __init__(self, name,color, weight):
    self.name=name
    self.color1=color
    self.weight= weight+10


class Person():
    def __init__(self, name, personnality, isSitting, robotowned):
        self.name=name
        self.personnality=personnality
        self.isSitting= isSitting
        self.robot=robotowned #la fction robot a ete defini plus haut
    
    def Presentation(self):
        print(f'''Hi, my name is {self.name}\n I m very {self.personnality} the name of my robot is {self.robot} and he is {self.color1}''')
        

    def SitDown(self):
        if self.isSitting==False:   # ca c'est la condition,
            self.isSitting=True  #on change (ou on donne) une nouvele valeur a notre varible pour faire asseoir
            print(f'{self.name} is now siiting down') 

    def Standup(self):
        if self.isSitting: #ici ==true
            self.isSitting=False
            print(f'{self.name} is standing')


r1= Robot('Tom', 'red', 65)
r2=Robot('jerry', 'blue', 45)
person1= Person('alice', 'aggressive', False, 'r2' )
person2= Person ('Becky', 'talakative', True, 'r1')

#p2.name pour acceder au nom p2  
# p2.robot c'est pour acceder a la classe de robot de p2
# pour acceder au nom du robot de p2=p2.robot.name          
person2.sitDown()
person1.standup()
SitDown()
Presentation()

