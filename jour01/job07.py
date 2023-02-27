class Personnage:
    def __init__(self, matrice, x, y ):
        self.matrice = matrice
        self.x = x
        self.y = y 
        self.positions = []

    def gauche(self):
        x_direction = 0
        y_direction = -1
        self.x += x_direction
        self.y += y_direction

    def droite(self):
        x_direction = 0
        y_direction = 1
        self.x += x_direction
        self.y += y_direction

    def bas(self):
        x_direction = 1
        y_direction = 0
        self.x += x_direction
        self.y += y_direction

    def haut(self):
        x_direction = -1
        y_direction = 0
        self.x += x_direction
        self.y += y_direction

    def position(self):
        self.positions.append((self.x, self.y))


p = Personnage(19, 4, 3)

p.bas()
p.position() 

p.haut()
p.position()

p.gauche()
p.position()

p.bas()
p.position()

print(p.positions)