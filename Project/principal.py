from numeros import *
from helper import *


def lista_menu():
    """muestra las secciones disponibles"""
    print(f"-- Saque su turno --")
    print(f"[1] Sección Farmacia\n"
          f"[2] Sección Perfumeria\n"
          f"[3] Sección Cosmética\n")


def operar_turnos(seccion, generador):
    """opera los turnos de esa seccion"""
    salir = False
    while not salir:
        Tools.clean()
        print(f"-- {seccion.upper()} --")
        print(next(generador))
        print(f"\n¿Desea más turnos de {seccion}? (Para cancelar escribe 'salir')")
        cancelar = input("<pulsa 'intro' para continuar> ")
        if cancelar == 'salir':
            salir = True
        else:
            salir = False


def elegir_opcion():
    """el usuario saca turno para una seccion"""
    while True:
        try:
            Tools.clean()
            lista_menu()
            turno = input("<seleccione una opcion> ")
            ['1', '2', '3'].index(turno)

        except ValueError:
            Tools.clean()
            print(f"-- Saque su turno --\n"
                  f"Error: Opcion no válida\n")
            input("<pulsa 'intro' para continuar> ")

        else:
            if turno == '1':
                decorar_turno(farmacia)
            elif turno == '2':
                decorar_turno(perfumeria)
            else:
                decorar_turno(cosmetica)
            break


def inicio():
    """Controla la ejecucion del programa"""
    continuar = True
    while True:
        try:
            Tools.clean()
            if continuar:
                elegir_opcion()
                print(f"¿Desea más turnos? (Para cancelar escribe 'salir')")
            else:
                print(f"-- Saque su turno --\n"
                      f"\n¿Desea más turnos? (Para cancelar escribe 'salir')")
            otro_turno = input("<pulsa 'intro' para continuar> ")
            ['salir', ""].index(otro_turno)
            continuar = True
        except ValueError:
            Tools.clean()
            print(f"-- Saque su turno --\n"
                  f"Error: Opcion no válida\n")
            input("<pulsa 'intro' para continuar> ")
            continuar = False
        else:
            if otro_turno == 'salir':
                Tools.clean()
                print(f"-- Saque su turno --\n"
                      f"Fin del programa\n")
                break


inicio()
