from moduls.load import *
from db.query import read
import os
import time

def modify(datos):
    os.system('cls')

    modify = input('- Enter the name of the album you want to modify for: ')

    for i, value in enumerate(arreglo):
        if modify.lower() == value.name.lower():  # Comparar ignorando mayúsculas/minúsculas
            new_name = input('- Get into name of Album: ')
            new_artist = input('- Get into Artist from album (or artists if collaborative album): ')
            new_gender = input('- Get into gender in album: ')

            cont = 1
            while cont > 0:
                new_rank = int(input('- Get into rank for album (1-10): '))
                if new_rank < 1 or new_rank > 10:
                    print('> rank not valid!')
                    cont = 1
                elif new_rank == 11:
                    print('> Broder, literally album is GOAT')
                    cont = 0
                else:
                    break

            time.sleep(.5)
            print('> Good, your album is saved!')
            print('_________________________________________________________________________')

            value.name = new_name
            value.artist = new_artist
            value.gender = new_gender
            value.rank = new_rank

            break

    else:
        print('- The album does not exist.')
