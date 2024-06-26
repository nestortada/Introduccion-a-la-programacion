print("Solicitar datos y si son divisibles por el ultimo numero ")
dato =[0 for rep in range(10)]
band = 0
for rep in range(10):
    print("Diga el dato #",rep +1)
    dato[rep] = int(input())
while dato[9] == 0 or dato[9]<0:
    print("Diga otro numero diferente de cero")
    dato[9]=int(input())
for rep in range(10):
    if dato[rep]%dato[9]==0:
        print("Hay numeros divisible por el umtimo numero")
        band = 1
if band == 0:
    print("No hay numeros divisibles por el ultimo numero")