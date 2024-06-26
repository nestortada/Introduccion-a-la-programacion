import random
print("Rifa")
personasN = [0 for rep in range(8)]
personasNu  = [0 for rep in range (8)]
aleatorio = random.randint(0,20)
print(aleatorio)
band = 0
for rep in range(8):
    print("La persona # ",(rep+1),"Diga su nombre")
    personasN[rep] = input()
    print("La persona",(rep +1),"Tambien diga un numero del uno al 20")
    personasNu[rep] = int(input())
    while personasNu[rep]<0 or personasNu[rep]>20:
        print("Valor invalido digite un  numero mayor a 0 o menor a 20 ")
        personasNu[rep] = int(input())
for rep in range(8):
    if personasNu[rep] == aleatorio:
        print("El jugador",personasN[rep],"Gano el premio")
        band = 1
if band == 0:
    print("Nadie gano el premio")
