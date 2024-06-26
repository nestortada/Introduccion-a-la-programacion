import matplotlib.pyplot as plt
x=[2,4,6,8,9]
y=[2,3,5,4,1]
y1=[1,9,10,12,5]
plt.bar(x,y,label="alumnos")
plt.bar(x,y1,width=0.5,label="pablación")
plt.legend()
plt.show()
