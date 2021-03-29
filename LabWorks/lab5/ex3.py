import math
from math import e
x = float(input("x="))
d=e**x
eps=float(input("Zadana Tochnist="))
s=1
a=x
b=1
c=1

while math.fabs(a/b)>eps:
    s+=a/b
    a*=x
    c+=1
    b=b*c
if d==S:
    print('Вірність справедлива')
else:
    print('Вірність не справедлива')
