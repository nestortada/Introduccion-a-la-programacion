print ("Analisis de un numero ")
mod=0
band = 0
print("Digite un numero ")
num= int(input())
while num<2:
    print("Valor invalido debe ser un valor entero y mayor o igual a dos(2)")
    num=int(input())
for rep in range(num):
    mod = mod+1
    if num%mod== 0 and mod>=2 and mod<num:
        band = 1
if band == 1:
    print("el numero no es primo")
else:
    print("El numero es primo")
if num%10000==0:
    print("Es multiplo dee 10000")
else:
    print("No es multiplo de 10000")
if num>=10000 and num<100000:
    print("el numero tiene 5 digitos")
else:
    print("El numero no tiene 5 digitos")
fact = 0
resp=1
for rep in range(num):
    fact = fact+1
    resp = resp*fact
print("El factorial de",num,"es ",resp)



