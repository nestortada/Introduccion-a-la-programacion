x=0
print("Evaluación de la tabla de multiplicación ")
def bienvenida():
    print("Escoja el numero de 1 a 10 para evaluar la tabla de multiplicar")
    x=int(input())
    while x<1 or x>10:
        print("Respuesta invalida diga un valor del 1 al 10")
        x=int(input())
    return x
def mult(x):
    acumt = " "
    for rep in range(21):
        acumt = acumt + str(x) + "*" + str(rep+1) +"=" + str(x*(rep+1))+ "\n"
    print(acumt)
def evalución(x):
    import random
    y=random.randint(1,20)
    print("Diga la respuesta de ",x," * ",y," = ")
    resp=int(input())
    if resp == x*y:
        print("Tuvisste la respuesta correcta ")
        cont=1
        return cont
    else:
        print("tuviste la respuesta incorrecta, la respuesta de ",x," * ",y," es igual a ",x*y)
        cont=0
        return cont
def presentar_nota(suma):
    print("Su nota de la evualución es de ",suma)


suma=0
cont=0
x = bienvenida()
mult(x)
for rep in range(5):
  cont= evalución(x)
  suma = suma+cont
presentar_nota(suma)