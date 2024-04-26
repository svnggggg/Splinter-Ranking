from moduls.load import *
from db.query import read
import os

def search(datos):
    os.system('cls')

    searching = input('- Enter the name of the album you want to search for: ')

    for i, value in enumerate(arreglo):
        if searching.lower() == value.name.lower():  # Comparar ignorando mayúsculas/minúsculas
            print('> Found this album!: ')
            print('# Name:', value.name)
            print('> Artist (or artists):', value.artist)
            print('> Gender:', value.gender)
            print('> Ranking:', value.rank)
            print('_________________________________________________________________________')
            break

    for i, human in enumerate(datos):
        if searching.lower() == human.name.lower():  # Comparar ignorando mayúsculas/minúsculas
            print('> Found this album!: ')
            print('# Name:', human.name)
            print('> Artist (or artists):', human.artist)
            print('> Gender:', human.gender)
            print('> Ranking:', human.rank)
            print('_________________________________________________________________________')
            return datos

    print('- The album does not exist.')
