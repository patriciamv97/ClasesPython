# TUPLAS E LISTAS

# Ejercicio 7.1

tupla1 = (1, 1, 5, 10)


def ordenar(tupla):
    if tupla[0] > tupla[1]:
        return "Mayor a menor"
    else:
        return "Menor a mayor"


print(ordenar(tupla1))


def ordenarBien(tupla):
    ordenar = True
    if len(tupla) > 1:
        for i in range(0, len(tupla) - 2):
            if tupla[i] > tupla[i + 1]:
                ordenar = False
                break
        return ordenar

    if not ordenar:
        print("Lista ordenada")
    else:
        print("Lista no ordenada")


ordenarBien(tupla1)


# Ejercicio 7.2


# Apartado 1
def domino(ficha1, ficha2):
    if set(ficha1) & set(ficha2):
        return "Las fichas encajan"
    else:
        return "Las fichas no encajan"


# print(domino((3, 4), (3, 5)))

# Apartado 2


def domino2(ficha1, ficha2):
    l1 = ficha1.split('-')
    l2 = ficha2.split('-')
    if set(l1) & set(l2):
        return "Las fichas encajan"
    else:
        return "Las fichas no encajan"


print(domino2("3-4", "4-5"))


# Resolución hecha por manuel

def resolucionDomino(ficha1, ficha2):
    encaixan = False
    if ficha1[0] == ficha2[0]:
        encaixan = True
    elif ficha1[0] == ficha2[1]:
        encaixan = True
    elif ficha1[1] == ficha2[0]:
        encaixan = True
    elif ficha1[1] == ficha2[1]:
        encaixan = True




# Ejercicio 7.3

# Apartado 1


t = ('Pepe', 'Manuela')

def campanha(nombres):
    for n in nombres:
        print("Estimado " + n)


# print(campaign(t))
campanha(t)

# Apartado 2
