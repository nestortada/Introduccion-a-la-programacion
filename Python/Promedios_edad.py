print("edad promdedio")
print("Cuantas persnas hay en el grupo")
personas = int(input())
menor = 0
mayor = 0
promediom = 0
promedioa =0
for rep in range(personas):
    print("cuntos años tiene",rep+1)
    edad = int(input())
    while edad < 0 or edad > 120:
        print("edad invalida, Diga nuevamente su edad")
        edad = int(input())

    if edad < 18:
        menor = menor + 1
        promediom = promediom + edad

    else:
        mayor = mayor + 1
        promedioa = promedioa + edad
if 0 < mayor:
    print("el promedio de mayor de edad es",(promedioa/mayor))
else:
    print("No hay mayores de edad")
if 0 < menor:
    print("El promedio de menor de edad es de",(promediom/menor))
else:
    print("No hay menores de edad")


