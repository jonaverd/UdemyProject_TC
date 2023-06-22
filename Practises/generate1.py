# Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números,
# iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next.

def secuencia_infinita():
    x = 0
    while True:
        x += 1
        yield x


generador = secuencia_infinita()
print(next(generador))
print(next(generador))