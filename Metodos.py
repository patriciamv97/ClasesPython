def saudar(lingua):
    def saudar_es():
        print("Hola")

    def saudar_gl():
        print("0la")

    funcion_saudar = {

        "es": saudar_es,

        "gl": saudar_gl

    }

    return funcion_saudar[lingua]


f = saudar("gl")

f()

saudar("es")()


# Funciones lambda

def suma(x, y):
    return x + y


def fun(x, y, z=1):
    return x + y - z


s = lambda x, y: x + y

print(suma(3, 2))
print(s(3, 2))

s1 = lambda x, y, z=1: (x + y) * z  # Si no se especifica el valor de z coje el valor asignado por nosotros

print(s1(2, 3, 2))
print(fun(2, 3, 2))

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 0]


def cadrado(n1):
    return n1 ** 2


l2 = map(lambda n1: n1 ** 2, l1)  # A cada elemento de la lista l  le aplica la funcion definida n**2

l3 = map(cadrado, l1)  # Esto es otra manera de modificar la lista , como l2, son equivalentes

for n in l2:
    print(n)

# Compresión de listas

l2 = [n ** 2 for n in l1]

print(l2)

l3 = [n for n in l1 if n % 2 == 0]

print(l3)

c = ['a', 'b', 'c']

l4 = [s * v for s in c
      for v in l1
      if v > 0]

print(l4)

# Xeradores

l5 = (n ** 2 for n in l1)
print(l5)


def meuXerador(n1, m, p1):
    while (n1 <= m):
        yield n1
        n1 += p1


xerador = meuXerador(7, 15, 2)

for n in xerador:
    print(n)

# for (int i=7; n<m; i+=p1)

for i in range(7, 15, 2):
    print(i)
