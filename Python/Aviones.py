import random
print("Dos aviones examen")
print("de cuantas filas quiere que sea su tabalero")
fila=int(input())
while fila<3:
    print("Diga un valor mayor a cero no se puede generar un valor con esto")
    fila=int(input())
print("Diga cuantas columnas quiere que sea su tablero ")
columna=int(input())
while columna<5:
    print("Diga un valor valor mayor a cero no se puede genrar un avion con esto ")
    columna=int(input())
def creartablero():
    tablero=[[" * " for rep in range(columna)] for rep in range(fila)]
    return tablero
def creaciondelavion(tablero):
    if fila <= 5:
        print("solo cabe un avion")
        x=2
        y = random.randint(1,3)
        tablero[y][x]= " p "
        tablero[y][x-1] = " X "
        tablero[y][x-2] = " X "
        tablero[y][x+2] = " X "
        tablero[y][x+1] = " X "
        tablero[y-1][x] = " X "
        tablero[y+1][x] = " X "
        return tablero
    else:
        contx=0
        conto=0
        contp=0
        while conto<6 or contx<6:
            x = random.randint(2,columna-3)
            y = random.randint(2,fila-3)
            x2=random.randint(2,columna-3)
            y2=random.randint(2,fila-3)
            tablero[y][x]= " p "
            tablero[y2][x2] = " p "
            tablero[y][x-1] = " X "
            tablero[y][x-2] = " X "
            tablero[y][x+2] = " X "
            tablero[y][x+1] = " X "
            tablero[y-1][x] = " X "
            tablero[y+1][x] = " X "
            tablero[y2][x2-1] = " O "
            tablero[y2][x2-2] = " O "
            tablero[y2][x2+2] = " O "
            tablero[y2][x2+1] = " O "
            tablero[y2-1][x2] = " O "
            tablero[y2+1][x2] = " O "
            for rep in range(fila):
                for i in range(columna):
                    if tablero[rep][i] == " X ":
                        contx=contx+1
                    if tablero[rep][i] == " O ":
                        conto= conto+1
        return tablero
def resultado(tablero):
    acum= "tablero"
    for rep in range(fila):
        acum = acum + "\n"
        for i in range(columna):
            acum = acum + str(tablero[rep][i])
    print(acum)
tablero=creartablero()
tablero=creaciondelavion(tablero)
resultado(tablero)