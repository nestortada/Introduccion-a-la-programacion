print("Temperaturas de dos dias")
temp1 = [0 for rep in range(24)]
temp2=[0 for rep in range (24)]
band =0
cont=0
dif =[0 for rep in range(24)]
horaA1=[0 for rep in range(24)]
horaA2 = [0 for rep in range(24)]
hora1 = 0
hora2 = 0
for rep in range(24):
    print("Digite la temperatura a la hora",rep+1)
    temp1[rep]=float(input())
    while temp1[rep]<-10 or temp1[rep]>40:
        print("temperatura invalida digite temperatura desde -10 hasta 40")
        temp1[rep]=float(input())
    if rep == 0:
        mayor1 = temp1[rep]
        mayorh1 = hora1
    if mayor1< temp1[rep]:
        mayor1 = temp1[rep]
        mayorh1 = hora1
    horaA1[rep] = hora1
    hora1 = hora1 +1
for rep in range(24):
    print("Digite las temperaturas del dia dos a la hora",rep+1)
    temp2[rep]=float(input())
    while temp2[rep]<-10 or temp2[rep]>40:
        print("temperatura invalida digite temperatura desde -10 hasta 40")
        temp2[rep] = float(input())
    if rep == 0:
        mayor2 = temp2[rep]
        mayorh2 = hora2
    if mayor2< temp2[rep]:
        mayor2 = temp2[rep]
        mayorh2 = hora2
    horaA2[rep] = hora2
    hora2 =  hora2 +1
for rep in range(24):
    if temp1[rep] != temp2[rep]:
        band = 1
        dif[cont] = temp1[rep]
        cont = cont+1
if band ==0 and cont == 0:
    print("Todas las horas de los dos dias tenian el mismo valor")
else:
    print("Hay diferencias entre los dos dias y son las siguientes")
    for rep in range(cont):
        pos = dif[cont]
        print(" en el dia uno ", temp1[pos],"Y en el dia dos ", temp2[pos], "a la hora ",horaA1[pos] )
if mayor1 > mayor2:
    print("El dia uno a la hora ",mayorh1-1, " es la temperarura mas grande de los dos dias con ", mayor1)
else:
    if mayor2 > mayor1:
        print("El dia uno a la hora ",mayorh2-1, " es la temperarura mas grande de los dos dias con ", mayor1)
    else:
        if mayor2 == mayor1:
            print("Tuvieron la misma la  alta temperatura los dos dias en el dia uno a las horas", mayorh1," y el dia dos a la hora", mayorh2," con una temperatura ", mayor2)