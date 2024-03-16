from load import *
from show import show
from search import search
from close import close
from db import read

datos: list[str] = read()

def main():
    '''
    Funcion la cual spawnea el menu del programa
    '''

    print('>>> Bienvenido a la Splinter Base')
    time.sleep(.5)
    cont = 1
    while cont > 0:
        print('1 - Cargar\n2 - Mostrar\n3 - Buscar\n4 - Salir\n')
        time.sleep(.5)
        menu = int(input('- Ingresa la opcion a la que deseas acceder: '))
        
        if menu == 1:
            cont = 1
            load(datos)
        elif menu == 2:
            cont = 1
            show(datos)
        elif menu == 3:
            cont = 1
            search(datos)
        elif menu == 4:
            cont = 0
            close()
            os.system('cls')
            print('> Gracias por ser usuario de la base Splinter B)')
        else:
            print('> Ingresa algo valido')

if __name__ == '__main__':
    main()

# · | Referencias |
# · # = Salida
# · - = Print or Intput
# · Importamos 'time' y 'os' para la estetica del programa
# · Importamos clase 'Persona' para que cada persona tenga sus atributos

# · if __name__ == '__main__': - Comprueba si el script se está ejecutando como programa principal.
# · los 'value.atributo' son los atributos de la persona que va a mostrar, los cuales estan almacenados en el arreglo!