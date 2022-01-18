import Pi
class Cercle():
    def __init__(self, radius=0, diameter=0):# si l'utilisateur entre le diametre, le rayon sera a zero, et vice versa
        self.radius=radius
        self.diameter=diameter
    def area(self):
        if self.diameter==0:
            return pi*self.radius