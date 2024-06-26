print("Analisis de numero ")
print("Diga un numero positivo entero mayor a uno")
primo= int(input())
mod = 0
while primo<2:
    print("numero invalido, Diga un numero positivo entero mayor a uno")
    primo = int(input())
for rep in range(primo):
    mod = mod +1
    if primo%mod == 0 and rep>1 and rep<(primo-1):
        primo=0
        print("No es un numero primo")
    else:
        if primo%mod ==0 and rep == (primo-1):
            print("es un numero primo")
if primo%10000!=0:
    print("El numer no es multiplo de 10000")
else:
    print("El mumero  es multiplo de 10000")