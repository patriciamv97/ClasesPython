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
# En python no son necesarios los metodos de acceso por que los atributos no tienen modificadores de visibilidad
p.getX()
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

    def getY(self):
        return self.__y

    def setX(self, x):
        if x > 0:
            self.__x = x
        else:
            self.__x = 0
            print("O valor é inicializado a cero")

    def setY(self, y):
        if y > 0:
            self.__y = y
        else:
            self.__y = 0
            print("O valor é inicializado a cero")

    def __eq__(self, outro):
        if self.x == outro and self.y == outro:
            return True
        else:
            return False

    x = property(getX, setX)
    y = property(getY, setY)


p2 = Punto2(3, 5)

# print(p2._Punto2__x)
# print(p2._Punto2__getY())

p2.x = 10

print(p2.x)

p2.y = 20

print(p2.y)

'''
__init__(self,args)
__new__(cls,args)
__del__(self)   borra un obxeto
__STR__(self) toString()
__cmp__(self,outro) Compara un obxeto con outro obxeto
'''

print(p2.__eq__(p))
print(p2 == p)
print(p2.__sizeof__())

