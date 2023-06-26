def decorar_turno(funcion):
    """Imprime informacion extra en el turno"""

    def informacion_adicional():
        print(f"\n{'*' * 40}")
        print(f"\tNº de ticket")
        print(f"\t{next(funcion)}")
        print(f"\tEspere hasta ser atendido")
        print(f"{'*' * 40}\n")

    return informacion_adicional()


def generador_farmacia():
    """Lleva la cuenta de los números de turnos para ese sector"""
    x = 100
    while True:
        x += 1
        yield f"F-{x}"


farmacia = generador_farmacia()


def generador_perfumeria():
    """Lleva la cuenta de los números de turnos para ese sector"""
    x = 100
    while True:
        x += 1
        yield f"P-{x}"


perfumeria = generador_perfumeria()


def generador_cosmetica():
    """Lleva la cuenta de los números de turnos para ese sector"""
    x = 100
    while True:
        x += 1
        yield f"C-{x}"


cosmetica = generador_cosmetica()
