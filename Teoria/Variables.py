print('Comentarios')

# Comentarios dunha linea
# O seu uso é para comentar instruccións ou partes do código
"""
Comentarios multilinea :
Utilizanse para documentar o 'código'

"""
'''
Podemos xerar manuais de uso para programadores do noso código 
O estilo de "Javadoc"
'''

print('Tipos básicos')

numero = 5
comaFlotante = 24.42
complexos = 7 + 2j
booleanos = True

print(type(complexos))
print(type(comaFlotante))
print(type(booleanos))

# O tipo das cadeas e string  (str)

cadeas = "Cadeas de texto"
cadea2 = str(complexos)
cadea3 = 'Outra cadea'

# Casteo de complex a string

print(type(str(complexos)))

# Concatenación

print(cadeas + " " + cadea3)

# Operadores

# Potencias
potencia = 2e2  # 2*10²
print(potencia)
potencia2 = 2 ** 2  # 2²

print(potencia2)

# División

div = 5.5 / 2
print(div)
divEnetira = 5.5 // 2
print(divEnetira)

# Módulo

modulo = 5.5 % 2
print(modulo)

# Operacions a nivel de bits

# & y lóxica

resultado = 3 & 2
print(resultado)

# ( 2 = 00000010 &  3 =00000011  ) = 00000010

# | o lóxica

resultado2 = 3 | 2

print(resultado2)

# ( 2 = 00000010 | 3 =00000011  ) = 00000011

# ^ o exclusiva

resultado3 = 3 ^ 2

print(resultado3)

# ( 2 = 00000010 ^ 3 =00000011  ) = 00000001

# ~ complementario El complemento a uno de un número binario se define como el valor obtenido al invertir todos los
# bits en la representación binaria del número (intercambiando 0 por 1 y viceversa). Los complementos del número se
# componen como el negativo del número original, en algunas operaciones aritméticas.

resultado4 = ~ 3

print(resultado4)

print(bin(3))
print(bin(~3))

# >> desplazado hacia la derecha , mueve los bit marcados una posicion hacia la derecha
# 3 =00000011   3 << 1 = 3  =00000010


resultado5 = 10 >> 1

print(resultado5)

# << desplazado a la izquierda , mueve los bit marcados una posicion hacia la izquiera
# 3 =00000011   3 >> 1 = 3  =00000110

resultado6 = 3 << 1

print(resultado6)

# Operaciones lóxicas and or not

print(True or False)
print(True and False)
print(not True)

# Coleccións : son estructuras de almacenamiento de datos
# Tipos de coleccións :

# 1) Listas:

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

l2 = [1, "Dous", 3 + 4j, [1, 2, 3]]

print(l1[2])

print(l2[1])

print(l1[-1])

print(l2[-1][2])

# Empieza por la derecha y accede al primer elemento que es  [1, 2, 3] y luego al segundo elemnto del array

print(l2[1][1])

print(l2[2])

l1[2] = 15.9999

print(l1)

print(l1[1:4])  # Muestra toda la lista menos los elementos en la posición 1 y 4
print(l1[1:-1:2])  # Marco inicio y fin y luego salto de dos en dos
print(l1[1:])  # Si no se pone nada se llega hasta el final
print(l1[1::2])
l1[4:7] = ["tres", "catro", "cinco"]
print(l1)
l1[4:7] = ["Cero"]
print(l1)

# Creando una lista y añadiendo elementos

l3 = list()
l4 = [0]
l5 = []
l3.append(1)
l4.append(0)
print(l3)
print(l4)
print(l5)
l5.append(1)
print(l5)

# Tuplas : las tuplas son coleccións estáticas, es decir , despois da creación non se pode modificar

t = (1, 2, "tres", [4, 5, 2 + 4j])  # A tupla se pode construir sen os parénteses por que o operador é a coma
print(t)
t2 = 2,  # Si no le pongo la coma lo pasa como un enteiro (t2 = 2 print(t2)----> 2)
print(t2)

'''
Esto da fallo por que no se pueden cambiar elemntos de una tupla
print(t[0])  
t[0] = 3
print(t)
'''
# Esto si o admite por que está cambiando un elemento dunha colección dinámica dentro dunha estática
t[3][1] = 9
print(t)

# Búcles

for elemento in t:
    print(elemento)

# Diccionarios

d = {
    1: "Un",
    2: "Dos",
    3: "Tres",
    "Patricia": "234564"
}

print(d[1])
print(d["Patricia"])
d["Patricia"] = "6532"
print(d)

print(d.items())
print(d.keys())
print(d.values())
print(d.get("Manuela", "Clave non encontrada"))
print(d.get("Patricia", "Clave non encontrada"))

# Métodos relacionados con listas

print(l1)

l1.append(10)  # Añade un elemento a la lista l1

print(l1)

print("Número de veces que aparece 10 co método count: " + str(l1.count(10)))  # Cuenta un elemento de una lista

print(len(d))  # Método que saca los elementos de cualquier coleccion

l1.extend((114, 115, 114, 116))  # Añades varios elementos

print(l1)

# print(l1.index(114))  # Para saber el índice de un elemento

print(l1.index(114, 10, 14))  # Para saber el índice de un elemento

l1.insert(10, 112)

print(l1)

print(l1.pop(10))  # Devuelve el valor dado un indice

l1.remove(115)  # Elimina un elemento

print(l1)

l1.reverse()  # Para mostrar la lista del reves

print(l1)

lista = ["Ola", "OOOla", "Hola", "HI"]


def ordea(x):
    return len(x)


lista.sort(key=ordea)

print(lista)

# Cadeas de caracteres

cadea = "Python para todos"

print(cadea[1:18:2])

print(cadea.count('o'))  # Cuenta todas as o que aparecen na cadea

print(len(cadea))  # Cuenta os caracteres da cadea

print(cadea.find('o', 5, 14))  # Ver si entre a posición 5 y 14 hay alguna o

cadena2 = cadea.join(('Ola ', ' a ', ' todos ', ' no ', ' presente ', ' curso.'))

print(cadena2)

print(cadea.partition(' '))

print(cadea.split(' '))

print(cadea.replace(' ', '_'))

print(cadea.upper())
