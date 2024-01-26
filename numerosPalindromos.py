"""Números palíndromos
Escriba la función invertir_digitos(n) que reciba un número entero n y entregue 
como resultado el número n con los dígitos en el orden inverso:
>>> invertir_digitos(142)
241
A continuación, escriba un programa que indique si el número ingresado 
es palíndromo o no, usando la función invertir_digitos:"""

def invertir_digitos(n):
    return int(str(n)[::-1])
num=int(input("ingresa tu numero: "))
if num==invertir_digitos(num):
    print(f"El numero {num} es un palindromo")
else:
    print(f"El numero {num} no es palindromo : {invertir_digitos(num)}")