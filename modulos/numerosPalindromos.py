from os import system
from .sistema.continuar import Cont

def invertir_digitos(n):
    return int(str(n)[::-1])
def palindromo():
    x=True
    while x:
        system("clear")
        print("""
            ============   Números palíndromos   ================

            Escriba la función invertir_digitos(n) que reciba un 
            número entero n y entregue como resultado el número 
            n con los dígitos en el orden inverso:
            invertir_digitos(142)
            241
            A continuación, escriba un programa que indique si 
            el número ingresado es palíndromo o no, usando la 
            función invertir_digitos:
            =====================================================""")
        num=int(input("\n\t-Escriba su numero: "))
        system("clear")
        if num==invertir_digitos(num):
            print(f"\n\t - El numero {num} es un palindromo")
        else:
            print(f"\n\t - El numero {num} no es palindromo : {invertir_digitos(num)}")
        x=Cont()
        
        