from moduls.load import *
from db.query import read
import os
import time

def remove(data):
    os.system('cls')

    removing = input('- Enter the name of the album you want to remove for: ')

    for i, value in enumerate(data):  # Itera sobre la lista 'data' en lugar de 'arreglo'
        if removing.lower() == value.name.lower():
            print('> Ok, you are removing album!')

            data.remove(value)  # Elimina el objeto 'value' de la lista 'data'

            time.sleep(.5)
            print('> Good, your album is removed!')
            print('_________________________________________________________________________')
            break

    else:
        print('- The album does not exist.')
