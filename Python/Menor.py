print("Menor del gupo")
print("Cauntas personas hay en su grupo")
personas=int(input())
while personas < 0:
    print("respuesta invalida diga un numero mayor o igual a cero")
    personas=int(input())
for rep in range(personas):
    print("Diga los años que tiene la persona # ",(rep+1))
    años = int(input())
    while años <= 0 or años>120:
        print("Edad invalida diga una edad mayor a 0 y menor a 120")
        años = int(input())
    print("Diga su nombre de la persona numero",(rep+1))
    nombre = input()
    if rep == 0:
        menor = nombre
        menora = años
    if menora > años:
        menor = nombre
        menora = años
print("El menor del grupo se llama ", menor)