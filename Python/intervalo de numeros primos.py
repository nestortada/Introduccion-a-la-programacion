print("Intervalo de numeros primos ")
print("elije el menor numero ")
contm=0
i=0
acum=" "
menor=int(input())
while menor<=1:
    print("Debe ser un numero mayor a uno")
    menor=int(input())
intervalome=menor
print("Elija el mayor")
mayor=int(input())
while mayor<menor:
    print("El numero que debe digitar debe ser mayor a ",menor)
    mayor=int(input())
intervaloma=mayor
while menor!=mayor+1:
    mod=0
    rep=0
    while rep<menor:
        mod=mod+1
        if menor%mod==0 and rep>0 and rep<(menor-1):
            rep = menor
        else:
            if menor%mod==0 and rep ==(menor-1):
                acum=acum+str(menor)+" "
                contm=contm+1
        rep = rep+1
    menor=menor+1
print("Los numeros primos del intervalo ",intervalome," hasta ",intervaloma," son: ",acum)
print("En el interavalo de ",intervalome," hasta ",intervaloma," hay ",contm," numeros primos")
