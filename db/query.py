from db.models import Album

def read():
    datos: list = []
    with open('data.txt', 'r') as arch:
        for i in arch:
            partes = i.strip().split(',')
            passed = Album(partes[0], partes[1], partes[2], int(partes[3]))
            datos.append(passed)
    return datos

