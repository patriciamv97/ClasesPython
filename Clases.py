class Punto:
    """Clase que define a un punto en un plano de duas dimensións"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x


class Circulo(Punto):  # Herencia
    def __init__(self, x, y, r):
        Punto.__init__(self, x, y)  # Inicializamos los valores de los atributos de la superclase
        self.r = r


p = Punto(1, 3)
c = Circulo(2, 3, 6)
print(
    p.getX())  # En python no son necesarios los metodos de acceso por que los atributos no tienen modificadores de visibilidad
print(p.x)
print(c.x)


class Punto2:

    """Clase que representa puntos no primeiro cuadrante
        Implica que x>0 e y>0
    """

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def __getY(self):
        return self.__y


p2 = Punto2(3, 5)

print(p2._Punto2__x)
print(p2._Punto2__getY())
