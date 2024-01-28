from os import system
from .sistema import validate, continuar
#Escriba la función es_divisible(n, d) que indique si n es divisible por d:
def es_divisible(n, d):
    if n%d==0:
        return True
    else:
        return False

#Usando la función es_divisible, escriba una función es_primo(n) que determine si un número es primo o no:
def es_primo(n):
    primo=True
    if n==2 or n==3:
        primo= True
    else:
        for i in range(2,n-1):
            if es_divisible(n,i):
                primo= False
    return primo

#Usando la función es_primo, escriba la función i_esimo_primo(i) que entregue el i
#-ésimo número primo.
def i_esimo_primo(i):
    x=0
    n=2
    primo=0
    while x<i:
        if es_primo(n):
            x+=1
            primo=n
        n+=1
    return primo

#Usando las funciones anteriores, escriba la función primeros_primos(m) que entregue una lista de los primeros m
#números primos:
def primeros_primos(m):
    lista=[]
    n=2
    while len(lista)<m:
        if es_primo(n):
            lista.append(n)
        n+=1
    return lista
#Usando las funciones anteriores, escriba la función primos_hasta(m)
#que entregue una lista de los primos menores o iguales que m
def primos_hasta(m):
    lista=[]
    n=2
    primo=0
    while n<=m:
        if es_primo(n):
            lista.append(n)
        n+=1
    return lista
print(primeros_primos(20))

def primosmenu():
    x=True
    while x:
        system("clear")
        print("""
            Funciones de números primos
            
        En los ejercicios para la materia del primer certamen, 
        usted debió desarrollar programas sobre números primos.

        Muchos de estos programas sólo tenían pequeñas diferencias 
        entre ellos, por lo que había que repetir mucho código al 
        escribirlos. En este ejercicio, usted deberá implementar algunos 
        de esos programas como funciones, reutilizando componentes para 
        evitar escribir código repetido.

        1- Imprima si los dos numeros son divisibles
        2- Descubra si su numero es primo
        3- imprima el i esimo numero primo
        4- Imprima la cantidad de primos:
        5- Imprimir primos menores o iguales a m:
        0- Salir
        """)
        opc=int(input("Escriba el numero del programa que quiera ejecutar: "))
        b=True
        while b:
            match(opc):
                case(1):
                    system("clear")
                    print(es_divisible(int(input("ingrese numero 1: ")),int(input("ingrese numero 2: "))))
                case(2):
                    system("clear")
                    print(es_primo(int(input("ingrese numero: "))))
                case(3):
                    system("clear")
                    print(i_esimo_primo(int(input("ingrese numero: "))))
                case(4):
                    system("clear")
                    print(primeros_primos(int(input("ingrese numero: "))))
                case(5):
                    system("clear")
                    print(primos_hasta(int(input("ingrese numero: "))))
                case(0):
                    system("clear")
                    x=False
                case(_):
                    validate.opcNo()
            b=(continuar.Cont())