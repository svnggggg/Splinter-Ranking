from load import *
from db import read

def search(datos):
        
    '''
        Funcion para buscar personas en base al DNI
    '''
    os.system('cls')
    cont = 1

    while cont > 0:
        searching = int(input('- Ingresa el DNI de la persona que buscas: '))
        if searching < 0:
            print('- DNI no valido, ingresa otro porfavor')
            cont = 1
        else:
            break

    for i, value in enumerate(arreglo):
        if searching == value.dni:
            print('- Encontre a la persona!')
            print('# Nombre:', value.nombre)
            print('> Apellido:', value.apellido)
            print('> DNI:', value.dni)
            print('> Edad:', value.edad)
            print('_________________________________________________________________________')
            return 1

    for i, human in enumerate(datos):
        if searching == human.dni:
            print('- Encontre a la persona!')
            print('# Nombre:', human.nombre)
            print('> Apellido:', human.apellido)
            print('> DNI:', human.dni)
            print('> Edad:', human.edad)
            print('_________________________________________________________________________')
            return datos
        print('- La persona no existe Bc')

