#Este es un ejemplo de python para git

class Cuadrado:
    def __init__(self, a, b):
        self.lado_a = a
        self.lado_b = b

    def area(self):
        return self.lado_a * self.lado_b

    def perimetro_2(self):
        return self.lado_a+self.lado_a+self.lado_a+self.lado_a

    def conflic(self):
        pass
