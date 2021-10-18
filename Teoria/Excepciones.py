import Clases

try:
    print(Clases.p2.y / 1)
except (ZeroDivisionError, SyntaxError):
    print("Erro: Non se pode facer división por cero")
except ValueError:
    print("Erro: Valores incorrectos")
else:
    print("A división realizouse correctamente")
finally:
    print("A división fixose ou non ")

