num = [0 for rep in range(10)]
print("Diga 10 numeros enteros para calcual, cauntos estos son mayores al mayor por la mitad")
for rep in range(10):
    print("digite el numero",rep+1)
    num[rep]=int(input())
    if rep == 0:
        mayor=num[rep]
    if mayor<num[rep]:
        mayor = num[rep]
prom = mayor/2
cont = 0
for rep in range(10):
    if prom<num[rep]:
        cont = cont + 1
print("La cantidad de numeros por encima de ", prom," son ",cont)