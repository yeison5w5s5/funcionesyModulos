from os import system
from .sistema.continuar import Cont
def par(num):
    system("clear")
    if num%2==0:
        return True
    else:
        return False
def num():
    x=True
    while x:
        system("clear")
        print("""
    Escriba la función par(x) que retorne 
    True si x es par, y False si es impar:
        """)
        numero= int(input("\n\t-Escriba su numero: "))
        print(f"\t == {par(numero)} == ")
        x=Cont()
