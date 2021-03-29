def gp(b,j):
    q1=b[j]/b[j-3]
    q2=b[j-1]/b[j-3]
    q3=b[j-2]/b[j-3]
    return q1==q2==q3
n = int(input('n='))
a = list(map(int,input().split()))
s=0
for el in range(3,n):
    s+=gp(a,el)
print(s)
