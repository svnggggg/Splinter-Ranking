from moduls.load import *
from db.query import read

def show(datos):
    os.system('cls')
    print('| Albums uploaded in this session |')
    for i, value in enumerate(arreglo): 
        print('> Name:', value.name)
        print('> Artist (or artists):', value.artist)
        print('> Gender:', value.gender)
        print('> Ranking:', value.rank)
        print('_________________________________________________________________________')

    print('| Albums upload in past sessions |')
    leer = open('data.txt','r')
    cont = 0
    for passed in datos:
        cont += 1
        print('> Name:', passed.name)
        print('> Artist (or artists):', passed.artist)
        print('> Gender:', passed.gender)
        print('> Ranking:', passed.rank)
    print('_________________________________________________________________________')

