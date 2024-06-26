print("Numeros positivos contador ")
seguir = "si"
cont = 0
while seguir == "si":
    print("Diga un numero")
    num = int(input())
    if num > 0:
        cont=cont+1
    print("Quiere seguir con el ejercicio")
    seguir =input()
    while seguir != "si" and seguir !="no":
        print("La respuesta es invalida, diga si o no ")
        print("Quiere seguir")
        seguir =input()
print("La cantidad de numeros positivos son",cont)
