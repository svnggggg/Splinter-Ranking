from db.models import Album 
import time
import os 

arreglo = []

def load(datos):
    os.system('cls')
    name = (input('- Get into name of Album: '))
    artist = (input('- Get into Artist from album (or artists if collaborative album) '))
    gender = (input('- Get into gender in album '))


    cont = 1
    while cont > 0:
        rank = (int(input('- Get into rank for album (1-10): ')))
        if rank < 0 or rank > 11:
            print('> Rank no valid!')
            cont = 1
        elif rank == 11:
            print('> Broder, literally album is GOAT')
            cont = 0
        else:
            break
    
    time.sleep(.5)
    print(' > Good, your album is saved!')

    album = Album(name,artist,gender,rank) # Carga un album en base a los atributos que cargo
    arreglo.append(album) # Mete al album en un arreglo
    print('_________________________________________________________________________')
    return datos
