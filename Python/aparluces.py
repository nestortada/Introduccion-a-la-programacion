import random
def bienbenida():
    print("El juego consiste que en el tablero te sale al lazar 5 corazones y para ganaar el jurgo lo que tienes que hacer es que todo el tablero este en diamantes "+"\n"+
          "Al poner una fila y columna tu simbolo va a cambiar de corazon a diamante o viceversa, ademas los simbolos de al lado donde lo decidiste cambiar tammbien cambia su signo(en una cruz se cambia )")
def creacion():
    cont=2
    tablero =[["♦" for i in range(5)] for rep in range(5)]
    while cont<5 :
        cont = 0
        tablero =[["♦" for i in range(5)] for rep in range(5)]
        for rep in range(5):
            fila = random.randint(0,4)
            columna = random.randint(0,4)
            tablero[fila][columna]= "♥"
        for rep in range(5):
            for i in range(5):
                if tablero[rep][i]=="♥":
                   cont = cont+1
    acum= "tablero"
    for rep in range(5):
        acum =  acum+ "\n"
        for i in range(5):
            acum = acum + str(tablero[rep][i]) + " . "
    print(acum )
    return tablero
def juego(tablero ):
    print("Elije una fila  para apagar para cambiar el simbolo ")
    fila = int(input())
    fila = fila -1
    while fila<0 or fila>5:
        print("Este valor es invalido diga un numero de 1 a 5  ")
        fila = int(input())
        fila = fila -1
    print("Elije una columna para cambiar de signo ")
    columna = int(input())
    columna = columna-1
    while columna<0 or columna>5:
        print("Este valor es invalido diga un numero entre 1 a 5")
        columna=int(input())
        columna= columna-1
    if tablero[fila][columna] == "♥":
        tablero[fila][columna] = "♦"
    else:
        tablero[fila][columna] = "♥"
    if columna == 0 and fila == 0:
        if tablero[fila][columna+1] == "♥":
            tablero [fila][columna+1] ="♦"
        else:
            tablero[fila][columna+1] = "♥"
        if tablero[fila+1][columna] =="♥":
            tablero[fila+1][columna] = "♦"
        else:
            tablero[fila+1][columna]="♥"
    if fila == 0 and columna>0 and columna<4:
        if tablero[fila][columna+1] == "♥":
           tablero[fila][columna+1] = "♦"
        else:
           tablero[fila][columna+1] = "♥"
        if tablero[fila+1][columna]=="♥":
            tablero[fila+1][columna]="♦"
        else:
            tablero[fila+1][columna]="♥"
        if tablero[fila][columna-1]=="♥":
            tablero[fila][columna-1]="♦"
        else:
            tablero[fila][columna-1]="♥"
    if fila == 0 and columna == 4:
        if tablero[fila][columna-1]=="♥":
            tablero[fila][columna-1]="♦"
        else:
            tablero[fila][columna-1]="♥"
        if tablero[fila+1][columna]=="♥":
            tablero[fila+1][columna]="♦"
        else:
            tablero[fila+1][columna]="♥"
    if columna==4 and fila>0 and fila<4:
        if tablero[fila+1][columna] =="♥":
            tablero[fila+1][columna]="♦"
        else:
            tablero[fila+1][columna] ="♥"
        if tablero[fila-1][columna]=="♥":
            tablero[fila-1][columna]="♦"
        else:
            tablero[fila-1][columna]="♥"
        if tablero[fila][columna-1]=="♥":
            tablero[fila][columna-1]="♦"
        else:
            tablero[fila][columna-1]="♥"
    if fila == 4 and columna == 4:
        if tablero[fila-1][columna]=="♥":
            tablero[fila-1][columna]="♦"
        else:
            tablero[fila-1][columna]="♥"
        if tablero[fila][columna-1]=="♥":
            tablero[fila][columna-1]="♦"
        else:
            tablero[fila][columna-1]="♥"
    if fila == 4 and columna>0 and columna<4:
        if tablero[fila-1][columna]=="♥":
            tablero[fila-1][columna]="♦"
        else:
            tablero[fila-1][columna]="♥"
        if tablero[fila][columna-1]=="♥":
            tablero[fila][columna-1]="♦"
        else:
            tablero[fila][columna-1]="♥"
        if tablero[fila][columna+1]=="♥":
            tablero[fila][columna+1]="♦"
        else:
            tablero[fila][columna+1]="♥"
    if fila == 4 and columna ==0:
        if tablero[fila][columna+1]=="♥":
            tablero[fila][columna+1]="♦"
        else:
            tablero[fila][columna+1]="♥"
        if tablero[fila-1][columna]=="♥":
            tablero[fila-1][columna]="♦"
        else:
            tablero[fila-1][columna]="♥"
    if fila>0 and fila<4 and columna == 0:
        if tablero[fila][columna+1]=="♥":
            tablero[fila][columna+1]="♦"
        else:
            tablero[fila][columna+1]="♥"
        if tablero[fila-1][columna]=="♥":
            tablero[fila-1][columna]="♦"
        else:
            tablero[fila-1][columna]="♥"
        if tablero [fila+1][columna] =="♥":
            tablero[fila+1][columna]="♦"
        else:
            tablero[fila+1][columna]="♥"
    if fila>0 and fila<4 and columna>0 and columna<4:
        if tablero[fila][columna+1]=="♥":
            tablero[fila][columna+1]="♦"
        else:
            tablero[fila][columna+1]="♥"
        if tablero[fila-1][columna]=="♥":
            tablero[fila-1][columna]="♦"
        else:
            tablero[fila-1][columna]="♥"
        if tablero [fila+1][columna] =="♥":
            tablero[fila+1][columna]="♦"
        else:
            tablero[fila+1][columna]="♥"
        if tablero[fila][columna-1]=="♥":
            tablero[fila][columna-1]="♦"
        else:
            tablero[fila][columna-1]="♥"
    return tablero
def mostrar(tablero):
    acum= "tablero"
    cont =0
    for rep in range(5):
        acum =  acum+ "\n"
        for i in range(5):
            acum = acum + str(tablero[rep][i]) + " . "
            if tablero[rep][i]=="♥":
                cont =cont+1
    print(acum )
    return cont
cont = 100
bienbenida()
tablero = creacion()
while cont!=0:
    tablero=juego(tablero)
    cont=mostrar(tablero)