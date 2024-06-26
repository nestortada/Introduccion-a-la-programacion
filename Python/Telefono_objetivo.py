print("Objetivo del telefonia")
rep = 0
per = 0
while rep<1000000:
    print("Nombre del donador ")
    nom=input()
    print("Cual es el monto que quiere donar")
    dona=int(input())
    while dona< 0:
        print("Valor invalido digite un numero mayor a cero")
        dona=int(input())
    if rep == 0:
        mejorn = nom
        mejord = dona
    if mejord<dona:
        mejorn = nom
        mejord = dona
    rep=rep+dona
    print("El porcentaje de la meta es de ",((rep*100)/1000000),"%")
    per = per +1
    print("El promedio de las donaciones es de ",rep/per,"$")
print("La persona que mas dono fue ", mejorn)

