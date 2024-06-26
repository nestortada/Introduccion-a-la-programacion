print("Numero factorial ")
print("Diga un numero factorial")
mult =1
factorial = int(input())
while factorial<0:
    print("El factorial es invalido diga un numero positivo")
    factorial =int(input())
for rep in range(factorial):
    if factorial>0:
     mult = (rep+1)*mult

if factorial==0:
    print("La respuesta es cero")
else:
    print(mult)

print("Finalizar")

