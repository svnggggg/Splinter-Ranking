from moduls.load import *

def close():
    data = open('data.txt','a')
    for i, value in enumerate(arreglo):
        value.dni = str(value.rank)

        data.write(f'{value.name},{value.artist},{value.gender},{value.rank}\n')
    data.close()