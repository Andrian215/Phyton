  
a=float(input("a="))
n=float(input("n="))
i=0
s=0
e=a
while i<n:
    i+=1
    s+=1/e
    e*=a+i
print(s)
