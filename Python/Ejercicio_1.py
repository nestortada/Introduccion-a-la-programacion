# Nestor Adnres Tabares David
# 5 / 9/2022
print("Nota")
print("Diga su nota ")
nota = float(input())
while nota < 0.0 or nota > 5.0:
    print("Nota invalida, diga nuevamente su nota")
    nota = float(input())
if nota > 4.0:
    print("Buena nota")
else:
    if nota > 3.0:
        print("la nota es regular")
    else:
        print("La nota fue mala")

