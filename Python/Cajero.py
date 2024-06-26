print("Parte dos del examen final")
print("Escriba un valor para darle la plata, este valor tiene que ser un nuemro con dos nuemros decimales ")
plata = float(input())
while plata < 0 or plata > 1000000.00:
    print("valor invalido escriba un nuemro entre 0 a 1000000.00")
    plata = float(input())
cont100 = 0
cont50 = 0
cont20 = 0
cont10 = 0
cont5 =0
cont2=0
cont1 = 0
cont050=0
cont025=0
cont010=0
cont005=0
cont001=0
cont = plata/0.01
while cont >= 10000.00:
    cont100 = cont100 +1
    plata = plata -100
    cont = plata/0.01
while cont >=5000 and cont<10000:
    plata = plata - 50
    cont50 = cont50 +1
    cont = plata/0.01
while cont>=2000 and cont<5000:
    cont20 = cont20 +1
    plata = plata -20
    cont = plata/0.01
while cont>=1000 and cont<2000:
    cont10 = cont10 +1
    plata = plata -10
    cont = plata/0.01
while cont>=500 and cont<1000:
    cont5 = cont5 +1
    plata = plata -5
    cont = plata/0.01
while cont>=200 and cont<500:
    cont2 = cont2 +1
    plata = plata -2
    cont = plata/0.01
while cont>=100 and cont<200:
    cont1 = cont1 +1
    plata = plata -1
    cont = plata/0.01
while cont>=50.00 and cont<100:
    cont050 = cont050 +1
    plata = plata -0.50
    cont = plata/0.01
while cont>=25.00 and cont<50.00:
    cont025 = cont025 +1
    plata = plata -0.25
    cont = plata/0.01
while cont>=25.00 and cont<50.00:
    cont025 = cont025 +1
    plata = plata -0.25
    cont = plata/0.01
while cont>=10.00 and cont<25.00:
    cont010 = cont010 +1
    plata = plata -0.10
    cont = plata/0.01
while cont>=5.00 and cont<10.00:
    cont005 = cont005 +1
    plata = plata -0.05
    cont = plata/0.01
cont001 = plata/0.01

print("NOtas")
print("La cantidad minima de billetes que se te va a devolver, de billetes de 100 son ",cont100)
print("La cantidad minima de billetes que se te va a devolver, de billetes de 50 son ",cont50)
print("La cantidad minima de billetes que se te va a devolver, de billetes de 20 son ",cont20)
print("La cantidad minima de billetes que se te va a devolver, de billetes de 10 son ",cont10)
print("La cantidad minima de billetes que se te va a devolver, de billetes de 5 son ",cont5)
print("La cantidad minima de billetes que se te va a devolver, de billetes de 2 son ",cont2)
print("Monedas")
print("La cantidad minima que se te va a devolver, de monedas de 1 son ",cont1)
print("La cantidad minima que se te va a devolver, de monedas de 0.50 son ",cont050)
print("La cantidad minima que se te va a devolver, de monedas de 0.25 son ",cont025)
print("La cantidad minima que se te va a devolver, de monedas de 0.10 son ",cont010)
print("La cantidad minima que se te va a devolver, de monedas de 0.05 son ",cont005)
print("La cantidad minima que se te va a devolver, de monedas de 0.01 son ",cont001)


