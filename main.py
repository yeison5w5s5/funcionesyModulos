from modulos import numeroPar, numerosPalindromos, FuncionesPrimos
from os import system
def menumain():
    system("clear")
    print("""
    == Modulos y Funciones ==
        
     1- Numero par
     2- Numeros palindromos
     3- Funciones de numeros primos
     4- Aproximacion de seno y coseno
     5- Tabla de verdad
     6- Maximo comun divisor
     7- Modulo de listas
     8- Numeros romanos
     9- Ruteo de funciones
     0- Salir

    =========================""")
while True:
    menumain()
    opc=int(input("\t-"))
    match(opc):
        case(1):
            system("clear")
            numeroPar.num()
        case(2):
            system("clear")
            numerosPalindromos.palindromo()
        case(3):
            system("clear")
            FuncionesPrimos.primosmenu()
        case(0):
            system("clear")
            print("\t == fin ==")
            break