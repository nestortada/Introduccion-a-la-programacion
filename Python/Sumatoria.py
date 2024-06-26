print("Sumatoria de 8X a la N")
print("Cual quiere que sea el valor de N")
n=int(input())
while n<0:
    print("Valor invalido digite un numero mayor a cero")
    n=int(input())
resp = 1
fact = 0
for rep in range(n):
    fact = fact +1
    resp = resp * fact
x=-1
suma = 0
for rep in range(resp+1):
    x = x +1
    mult = 8*x**n
    suma =suma +mult
print("El resultado de la sumatoria es de ", suma)