from load import *
from db import read

def show(datos):
    '''
    Esta funcion muestra lo cargado y no cargado del txt!
    '''

    os.system('cls')
    print('| Personas cargadas rigth now |')
    for i, value in enumerate(arreglo): 
        print('> Nombre:', value.nombre)
        print('> Apellido:', value.apellido)
        print('> DNI:', value.dni)
        print('> Edad:', value.edad)
        print('_________________________________________________________________________')

    print('| Personas cargadas anteriormente |')
    leer = open('data.txt','r')
    cont = 0
    for human in datos:
        cont += 1
        print('> Nombre', human.nombre)
        print('> Apellido', human.apellido)
        print('> DNI', human.dni)
        print('> Edad', human.edad)
    print('_________________________________________________________________________')

