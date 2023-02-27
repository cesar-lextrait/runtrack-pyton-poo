class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def afficherlesPoints(self):
        print(self.x, self.y)

    def afficherX(self):
        print(self.x)
    
    def afficherY(self):
        print(self.y)

    def changerX(self, nouveau):
        self.x = nouveau     
        print(self.x)   
    
    def changerY(self, nouveau):
        self.y = nouveau
        print(self.y)


A = Point(2, 4)
A.afficherlesPoints()
A.afficherX()
A.afficherY()
A.changerX(9)
A.changerY(10)