import random
iniciox = 4
inicioy=4
colax = 5
colay = 4
def bienvenida():
    print("reglas del juego ")
def creacion():
  tablero =[["[🕸]" for i in range(10)] for rep in range(10)]
  contm =0
  contc = 0
  while contm!=20 or contc!=10:
    tablero =[["[🕸]" for i in range(10  )] for rep in range(10)]
    contm= 0
    contc= 0
    for rep in range(20):
        fila = random.randint(0,9)
        columna = random.randint(0,9)
        tablero[fila][columna] = "[💀]"
    for rep in range(10):
        fila = random.randint(0,9)
        columna = random.randint(0,9)
        tablero[fila][columna]="[🐾]"
    tablero[iniciox][inicioy]="[🐍]"
    tablero[colax][colay]="[🐊]"
    for rep in range(10):
        for i in range(10):
            if tablero[rep][i] == "[💀]":
                contm = contm + 1
            if tablero[rep][i]=="[🐾]":
                contc = contc + 1
  acum= "tablero"
  for rep in range(10):
      acum = acum + "\n"
      for i in range(10):
          acum = acum + str(tablero[rep][i])
  print(acum)
  return tablero
def paso():
    paso=input()
    while paso != "w" and paso != "s" and paso != "a" and paso != "d" and paso!= "t" :
        paso=input()
    return paso
def mapa(tablero):
    tablero[colax][colay]="[🕸]"
    return tablero
def choque(mov):
    if (mov == "w" or mov== "a") and inicioy==0 and iniciox==0:
        juego=0
        return juego
    else:
        if mov == "w" and iniciox ==0 and inicioy>0 and inicioy<9:
            juego=0
            return juego
        else:
            if (mov == "w" or mov =="d") and iniciox==0 and inicioy == 9:
                juego=0
                return juego
            else:
                if mov == "d" and iniciox>0 and iniciox<10 and inicioy== 9:
                    juego =0
                    return juego
                else:
                    if (mov == "s" or mov == "d") and iniciox==9 and inicioy==9:
                        juego =0
                        return juego
                    else:
                        if mov == "s" and  iniciox==9 and inicioy>0 and inicioy<9:
                            juego =0
                            return juego
                        else:
                            if(mov == "s" or mov =="a") and iniciox==9 and inicioy==0:
                                juego=0
                                return juego
                            else:
                                if mov== "a" and iniciox>0 and iniciox<9 and inicioy== 0:
                                    juego=0
                                    return juego
                                else:
                                    juego=1
                                    return juego
def morir(sigue):
    if inicioy==acolay  and iniciox==acolax:
        juego=0
        return juego
    else:
        juego=sigue
        return juego
def juego(mov,tablero):
    if mov == "w":
        tablero[iniciox][inicioy] ="[🐍]"
        tablero[colax][colay]="[🐊]"
        return tablero
    else:
        if mov == "s":
            tablero[iniciox][inicioy] = "[🐍]"
            tablero[colax][colay] ="[🐊]"
            return tablero
        else:
            if mov == "a":
                tablero[iniciox][inicioy] ="[🐍]"
                tablero[colax][colay] = "[🐊]"
                return tablero
            else:
                tablero[iniciox][inicioy] = "[🐍]"
                tablero[colax][colay] = "[🐊]"
                return tablero
def comida(tablero):
    contc=0
    for rep in range(10):
        for i in range(10):
            if tablero[rep][i]=="[🐾]":
                contc=contc+1
            else:
                if tablero[rep][i]=="[💀]":
                    contc =contc-1
    return contc
def num():
    x=random.randint(5,15)
    return x
def comprobar(tablero):
    cont = 0
    for rep in range(10):
        for i in range(10):
            if tablero[rep][i] == "[💀]":
                cont = cont + 1
    if cont == 20:
        bandera = 1
        return bandera
    else:
        bandera = 0
        return bandera
    
def mostrar(tablero,x):
    acum= "tablero"
    for rep in range(10):
        acum = acum + "\n"
        for i in range(10):
            acum = acum + str(tablero[rep][i])
    print(acum)
    print("Llevas en al putuación ",fruta," y para que se te cambien las huellas se en  ",x," jugadas")
def acabar():
    print("se termino el juego con una puntuacion de  ",fruta," frutas y ",rep," jugadas")
bandera =1
rep = 0
bienvenida()
tablero=creacion()
fruta=0
cambio = 1
contt=10
mov="w"
x=10
while bandera == 1:
    tpaso=mov
    acolax=colax
    acolay=colay
    mov = paso()
    tablero=mapa(tablero)
    colax = iniciox
    colay = inicioy
    sigue=choque(mov)
    if mov == "t":
        if tpaso=="w":
            mov=tpaso
            for rep in range(3):
                tablero=mapa(tablero)
                colax=iniciox
                colay=inicioy
                sigue=choque(mov)
                iniciox=iniciox-1
                if sigue == 1:
                    tablero=juego(mov,tablero)
                    contc=comida(tablero)
                    if contc<contt:
                        fruta=fruta+1
                        contt=contc
        else:
            if tpaso=="s":
                mov=tpaso
                for rep in range(3):
                    tablero=mapa(tablero)
                    colax=iniciox
                    colay=inicioy
                    sigue=choque(mov)
                    iniciox=iniciox+1
                    if sigue == 1:
                        tablero=juego(mov,tablero)
                        contc=comida(tablero)
                        if contc<contt:
                            fruta=fruta+1
                            contt=contc
            else:
                if tpaso=="a":
                    mov=tpaso
                    for rep in range(3):
                        tablero=mapa(tablero)
                        colax=iniciox
                        colay=inicioy
                        sigue=choque(mov)
                        inicioy=inicioy-1
                        if sigue == 1:
                            tablero=juego(mov,tablero)
                            contc=comida(tablero)
                            if contc<contt:
                                fruta=fruta+1
                                contt=contc
                else:
                    if tpaso=="d":
                        mov=tpaso
                        for rep in range(3):
                            tablero=mapa(tablero)
                            colax=iniciox
                            colay=inicioy
                            sigue=choque(mov)
                            inicioy=inicioy+1
                            if sigue == 1:
                                tablero=juego(mov,tablero)
                                contc=comida(tablero)
                                if contc<contt:
                                    fruta=fruta+1
                                    contt=contc
    else:
        if mov == "w":
            iniciox=iniciox-1
        else:
            if mov == "s":
                iniciox=iniciox+1
            else:
                if mov=="a":
                    inicioy=inicioy-1
                else:
                    inicioy=inicioy+1
    sigue=morir(sigue)
    if sigue == 1:
        tablero=juego(mov,tablero)
        contc=comida(tablero)
        if contc<contt:
            fruta=fruta+1
            contt=contc
        bandera = comprobar(tablero)
        mostrar(tablero,x)
        rep = rep +1
    else:
        print("Se muerto serpiente 💀💀")
        bandera=0
acabar()
