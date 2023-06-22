# Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea llamado:
#     "Te quedan 3 vidas"
#     "Te quedan 2 vidas"
#     "Te queda 1 vida"
#     "Game Over"
# Almacena el generador en la variable perder_vida

def generador():
    vidas = 4

    while True:
        vidas -= 1
        yield vidas


def comprobar(vidas):
    if vidas == 3:
        print("Te quedan 3 vidas")
    elif vidas == 2:
        print("Te quedan 2 vidas")
    elif vidas == 1:
        print("Te quedan 1 vida")
    else:
        print("Game Over")


perder_vida = generador()
actual = next(perder_vida)
comprobar(actual)
actual = next(perder_vida)
comprobar(actual)
actual = next(perder_vida)
comprobar(actual)
actual = next(perder_vida)
comprobar(actual)

# solucion sencilla
# def mensaje():
#     x = "Te quedan 3 vidas"
#     yield x
#
#     x = "Te quedan 2 vidas"
#     yield x
#
#     x = "Te queda 1 vida"
#     yield x
#
#     x = "Game Over"
#     yield x
#
#
# perder_vida = mensaje()
