from models import Persona

def read():
    datos: list = []
    with open('data.txt', 'r') as arch:
        for i in arch:
            partes = i.strip().split(',')
            human = Persona(partes[0], partes[1], int(partes[2]), int(partes[3]))
            datos.append(human)
    return datos

