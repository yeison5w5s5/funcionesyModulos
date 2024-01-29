#1- Escriba la función factorial_reciproco(n), que retorne el valor 1/n!.

def factorial_reciproco(n):
    resul= 1
    for i in reversed(range(n+1)):
        if i>1:
            resul*=i
    n=1/resul
    return n

# 2- Escriba la función signo(n) que retorne 
#    1 cuando n es par y −1cuando n es impar.
def signo(n):
    if n%2==2:
        return 1
    else:
        return -1

# 3- Escriba las funciones seno_aprox(x, m) y coseno_aprox(x, m)
#que aproximen respectivamente el seno y el coseno usando los m primeros 
#términos de las sumas correspondientes. Las funciones deben llamar a las
#funciones factorial_reciproco y signo.
    
def seno_aprox(x, m):
    b=1
    total=0
    for i in range(m):
        total+=signo(i)*(x**b)/factorial_reciproco(b)
        print()
        b+=2
    return total
def coseno_aprox(x, m):
    b=0
    total=0
    for i in range(m):
        total+=signo(i)*(x**b)/factorial_reciproco(b)
        b+=2
print(seno_aprox(30,4))
# 4 - Escriba la función error(f_exacta, f_aprox, m, x) que entreguen cuál
#es la diferencia entre el valor exacto de la función f_exacta y su
#aproximación con m términos usando la función f_aprox en x=x.