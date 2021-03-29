from math import sin,cos
n=float(input("n=")
x0=1
x1=1
i=1
while i<n:
    i+=1
    x2=sin(x1)+x0/cos(x1)
    x0=x1
    x1=x2
s=x2
print("Сума={0}".format(s))
