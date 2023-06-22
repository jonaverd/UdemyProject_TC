# Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7,
# iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).

def secuencia_infinita():
    x = 1
    while True:
        yield x*7
        x += 1


generador = secuencia_infinita()
print(next(generador))
print(next(generador))