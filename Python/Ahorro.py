
def menu():
    print("""Digite la opcion 1 para incrementar el ahorro
          Digete 2 para sacar el ahorro 
          Digite 3 para consultar el ahorro
          Digite 4 para terminar el programa""")
    opcion=int(input())
    return opcion
def ahorro ():
    print("Digite la cantidad que desea incrementar")
    incrementar = int(input())
    if incrementar<100:
        print("Respuesta invalida debe ser mayor a 100 peses")
        incrementar=0
    return incrementar
def sacar(incrementar):
    if incrementar>0:
        print("cuanto desea sacar: ")
        plata = int(input())
        if plata<0:
            print("Respuesta invalida, debe sacar un numero superior a 0")
            plata=0
            return plata
        else:
            total = incrementar-plata
            if total<incrementar/2:
                print("No se puede sacar plata debe ser debe ser igual o mayor a lo que usted tiene ahorrado ")
                plata=0
                return plata
        return plata
    else:
        print("No se puede ejecutar no tiene nada ahorrado")
def consultar(plata,incrementar):
    total = incrementar-plata
    print("El ahorro que usted tiene en la cuenta es de",total)
incrementar = 0
plata=0
opcion =2
while opcion != 4:
    opcion =menu()
    if opcion == 1:
        incrementar = ahorro()
    else:
        if opcion == 2:
            plata = sacar(incrementar)
        else:
            if opcion ==3:
                consultar(plata,incrementar)



