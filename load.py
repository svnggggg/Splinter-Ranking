from models import Persona 
import time
import os 

arreglo = []

def load(datos):
    '''
    Esta funcion va a cargar una persona,
    la cual va a ser guardada como objeto para luego sumarse al arreglo
    '''

    os.system('cls')
    nombre = (input('- Ingesa un nombre: '))
    apellido = (input('- Ingresa un apellido: '))
    
    cont = 1
    while cont > 0:
        dni = (int(input('- Ingresa un dni: ')))
        if dni < 0:
            print('> DNI no valido, ingresa otro porfavor')
            cont = 1
        else:
            break

    edad = (int(input('- Ingresa una edad: ')))
    persona = Persona(nombre,apellido,dni,edad) # Carga una persona en base a los atributos que cargo
    arreglo.append(persona) # Mete a persona en un arreglo
    print('_________________________________________________________________________')
    return datos
