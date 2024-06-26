def bienvenida():
    print("aniquilación Marciana ")
    print("cuenta con un tablero de 20 posiciones, en cada posicion hay 5 marcianos y usted cuenta con 5 bombas apara aniquilarlos,"+"\n"+"donde caiga se aniquila todos los marcianos, en las posiciones de al lado se aniquilan dos y en las posisciones que le siguen a esta se aniquilan uno ")
    mar=[5 for rep in range(20)]
    return mar
def bomba(mar):
    print("En que posicion quiere lanzar la bomba")
    bomba=int(input())
    while bomba<1 or bomba>20:
        print("Respuesta invalida, debe digitar un numero del 1 al 20")
        bomba=int(input())
    bomba = bomba - 1
    mar[bomba]=mar[bomba]-5
    if bomba == 19:
        mar[bomba-1]=mar[bomba-1]-2
        mar[bomba-2]=mar[bomba-2]-1
    else:
        if bomba==18:
            mar[bomba-1]=mar[bomba-1]-2
            mar[bomba-2]=mar[bomba-2]-1
            mar[bomba+1]=mar[bomba+1]-2
        else:
            if bomba==0:
                mar[bomba+2]=mar[bomba+2]-1
                mar[bomba+1]=mar[bomba+1]-2
            else:
                if bomba == 1:
                    mar[bomba+2]=mar[bomba+2]-1
                    mar[bomba+1]=mar[bomba+1]-2
                    mar[bomba-1]=mar[bomba-1]-2
                else:
                    mar[bomba+2]=mar[bomba+2]-1
                    mar[bomba+1]=mar[bomba+1]-2
                    mar[bomba-1]=mar[bomba-1]-2
                    mar[bomba-2]=mar[bomba-2]-1
    for rep in range(20):
        if mar[rep]<0:
            mar[rep]=0
    return mar
def informe(can,sumatoria):
    acum ="El tablero "
    sumatoria=0
    for rep in range(20):
        sumatoria = sumatoria + can[rep]
        acum = acum + " . " + str(can[rep])
    print("El porcentaje de los marcianos que quedan visvos son ",sumatoria,"%",acum)
    return sumatoria
sumatoria=100
mar= bienvenida()
while sumatoria>0:
    can=bomba(mar)
    sumatoria=informe(can,sumatoria)

