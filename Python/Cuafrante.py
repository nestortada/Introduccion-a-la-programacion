print("cuadrantes")
print("Diga la coordenada en X")
x = float(input())
while x == 0:
    print("la coordenada x no puede estar en el eje, diga otro numero")
    x = float(input())
print("Diga la coordenada de y")
y = float(input())
while y ==0:
    print("La coordenada y no puede estar en el eje, diga otro numero")
    y = float(input())
if x>0 and y>0:
    print("El cuadrante de X y Y esta en el 1")
else:
    if x<0 and y<0:
        print("El cuandrante de X y Y esta en el 3 ")
    else:
        if x>0 and y<0:
                print("El cuadrante de X y Y esta en el c4")
        else:
            print("El cuadrante de X y Y esta en el 2")