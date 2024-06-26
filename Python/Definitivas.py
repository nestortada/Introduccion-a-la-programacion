print("Definitivas")
cont =0
contr =0
for rep in range(15):
    print("Diga la efinitiva del estudiante #",(rep+1))
    nota = float(input())
    while nota<0.0 or nota>5.0:
        print("Nota incorrecta, diga una nota de 0.0 hasta 5.0")
        nota =float(input())
    if nota >= 3.0:
        cont= cont+1
    else:
        contr = contr+1
print("El porcentaje de estudiantes que reprobaron fueron ",(contr/15)*100,"%")
print("El numero de estudiante que aprobaron fueron de ",(cont/15)*100,"%")
