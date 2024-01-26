"""Escriba la función par(x) que retorne True si x es par, y False si es impar:"""
def par(num):
    if num%2==0:
        return True
    else:
        return False
par(input("Escriba su numero: "))