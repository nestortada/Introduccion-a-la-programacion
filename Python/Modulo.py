def bienvenida():
    print("Area y perimetro de un rectangulo")
def dato_solicitar():
    print("Diga dimensión del rectangulo")
    dato1 = float(input())
    while dato1 <=0:
        print("valor invalido, diga un numero mayor a 0")
        dato1=float(input())
    return dato1
def realizar_operacion(dato1, dato2):
    area = dato1*dato2
    return area
def realizar_perimetro(dato1,dato2):
    perimetro = 2*dato1 + 2*dato2
    return perimetro
def presentar_resultado(dato1,dato2,area,perimetro):
    print("El area de la dimension",dato1," ",dato2," es igual a",area)
    print("El perimetro de la dimensión ",dato1, " ",dato2," es igual a ",perimetro)
def operar(dato1,dato2):
    area = realizar_operacion(dato1,dato2)
    perimetro = realizar_perimetro(dato1,dato2)
    presentar_resultado(dato1,dato2,area,perimetro)
bienvenida()
dato1 = dato_solicitar()
dato2 = dato_solicitar()
operar(dato1,dato2)
