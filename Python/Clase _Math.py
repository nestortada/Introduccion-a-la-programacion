import math
print("Funciones matematicas ")
opcion = 2
while opcion != 0:
    print("Diga 1 si quiere valores de Pi"
        "Diga 2 para el valor de E;"
        "Diga 3 para el valor absoluto; "
        "Diga 4 para conversion de radianes a grados; "
        "Diga 5 para calcular funciones trigonometricas;"
        "Diga 6 para calcular raiz de un numero;"
        "Diga 7 para el valor de una potencia"
        "Diga 8 para redondiar un numero;"
        "Diga 9 para calcular hipotenusa "
        "Diga 0 si quiere salir")
    opcion=int(input())
    while opcion<0 or opcion>9:
        print("Diaga un valor de 0 a 10")
        opcion=int(input())
    if opcion == 1:
        print("El valor de pi es igual a ", math.pi,"Para este ejercicio utilice la libreria math.pi")
    else:
        if opcion == 2:
            print("El valor de E es ", math.e, "Para esta función utilice la libreria math.e")
        else:
            if opcion == 3:
                print("Diga un numero para el valor absoluto")
                num = float(input())
                print("El valor absoluto de ",num,"es igual a ",abs(num),"Para esta funcion utilice la libreria abs(x)")
            else:
                if opcion == 4:
                    print("Convertir de ranianes a grados, diga un valor")
                    num1=float(input())
                    print("El valor de ",num1,"es igual a ",math.degrees(num1),"Para esta función utilice la libreria math.degrees(x)")
                else:
                    if opcion == 5:
                        print("calcular el valor de seno, coseno y tangente, Diga un valor en grados")
                        num2=float(input())
                        print("El seno del valor de ",num2," es igual a ",math.sin(num2),"Para esta función utilice la función math.sin(x)")
                        print("El coseno del valor de ",num2," es igual a ",math.cos(num2),"Para esta función utilice la función math.cos(x)")
                        print("La tangente del valor de ",num2," es igual a",math.tan(num2),"Para esta función utilice la función math.tan(x)")
                    else:
                        if opcion == 6:
                            print("Diga un numero para calcular la raiz caudrada de este")
                            num3=int(input())
                            while num3<0:
                                print("valor invalido digite otro numero mayor o igual a cero")
                                num3=int(input())
                            print("el valor de ",num3," en raiz cuadrada es igual a ",math.isqrt(num3),"Para esta función utilice la función math.isqrt(x)")
                        else:
                            if opcion == 7:
                                print("Calcular una petencia ")
                                print("Diga la base")
                                base = float(input())
                                print("Diga la potencia a la que se quiere elevar")
                                pte=float(input())
                                print("El valor en base ",base," elevado a la ",pte," es igual a ",math.pow(base,pte),"Para esta función utilice la función math.pow(x,y)")
                            else:
                                if opcion == 8:
                                    print("Digite un valor para redondiar un numero hacia el entero menor")
                                    num4=float(input())
                                    print("el numero ", num4," hacia el entero mas abajo es ",math.floor(num4),"Para esta función utilice la función math.floor(x)")
                                else:
                                    if opcion == 9:
                                        print("Calcular un triangulo")
                                        print(" Diga el cateto uno")
                                        c1= float(input())
                                        c1 = abs(c1)
                                        print("Diga el cateto dos")
                                        c2 = float(input())
                                        c2 = abs(c2)
                                        print("La hipotenusa de ",c1," y ",c2," es igual a ",math.hypot(c1,c2),"Para esta función utilice la función math.hypot(x,y)")




