import matplotlib.pyplot as plt
print("Encuesta de animal")
n="si"
contg=0
contp = 0
contl =0
contt = 0
while n == "si":
    print("Cual es tu animal favorito: Gatos, Perros, Loros, Otros")
    ani=input()
    while ani != "gatos" and ani != "perros" and ani != "loros" and ani != "otros":
        print("Solo puede escribir: gatos,perros,loros o otros, todo en minuscula")
        ani =input()
    if ani =="gatos":
        contg = contg+1
    else:
        if ani =="perros":
            conrp =contp+1
        else:
            if ani == "Loros":
                contl = contl +1
            else:
                if ani == "otros":
                    contt=contt+1
    print("Hay mas gente en la sala")
    n=input()
    while n != "si" and n != "no":
        print("Respuesta invalida diga si o no en minuscula")
        n=input()
x =[contg,conrp,contl,contt]
y =["Gatos","Perros","Loros","otros"]
plt.pie(x,labels=y,shadow=True)
plt.show()

