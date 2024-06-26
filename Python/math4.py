import matplotlib.pyplot as plt
x=[2,4,6,8,9]
y=["Leo","JP","Nata","La profe","Cepegoat"]
ex=(0,0,0.2,0,0)
plt.pie(x,labels=y,explode=ex,shadow=True,startangle=180)
plt.show()
