print("Sumatoria de X=0 hasta n a la n de (8*(x*x)- ((4*x)/3)")
print("Digite el valor de n")
n=int(input())
while n<=0:
    print("Respuesta invalida digite el valor de n mayor a cero")
    n=int(input())
sumatoria = 0
x = 0
for rep in range((n**n)+1):
    sumatoria = (8*(x*x))-((4*x)/3) + sumatoria
    x = x +1
print("La respuesta de la sumatoria hasta ",(n**n)," es igual a ", sumatoria)
