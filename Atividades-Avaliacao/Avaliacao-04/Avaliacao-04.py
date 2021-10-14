class ponto:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def getx(self):
        return float(self.x)

    def gety(self):
        return float(self.y)

    def setx(self, x):
        self.x = float(x)

    def sety(self, y):
        self.y = float(y)

class reta:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def geta(self):
        return self.a.getx(), self.a.gety()
    def getb(self):
        return self.b.getx(), self.b.gety()
    def distancia(self):
        print("A distancia entre os pontos: \"{}\" e \"{}\" é de : ({}, {})!".format(
            self.geta(), self.getb(),
            self.a.getx()-self.b.getx(), self.a.gety()-self.b.gety()))

ponto1 = ponto(10, 3)
ponto2 = ponto(2, 1)

reta1 = reta(ponto1, ponto2)

reta1.distancia()