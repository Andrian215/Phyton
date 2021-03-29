def local():
    b=[]
    for i in range(1,n-1):
        for j in range(1,n-1):
            if a[i][j]<a[i-1][j] and a[i][j]<a[i][j-1] and a[i][j]<a[i][j+1] and a[i][j]<a[i+1][j] and n>2:
                b.append(a[i][j])
    for i in range(n-(n-1)):
        for j in range(1,n-1):
            if a[i][j]<a[i][j-1] and a[i][j]<a[i][j+1] and a[i][j]<a[i+1][j] and n>2:
                b.append(a[i][j])
    for i in range(n-1,n):
        for j in range(n-1):
            if a[i][j]<a[i][j-1] and a[i][j]<a[i][j+1] and a[i][j]<a[i-1][j] and n>2:
                b.append(a[i][j])
    for i in range(1,n-1):
        for j in range(n-(n-1)):
            if a[i][j]<a[i-1][j] and a[i][j]<a[i][j+1] and a[i][j]<a[i+1][j] and n>2:
                b.append(a[i][j])
    for i in range(1,n-1):
        for j in range(n-1,n):
            if a[i][j]<a[i-1][j] and a[i][j]<a[i][j-1] and a[i][j]<a[i+1][j] and n>2:
                b.append(a[i][j])
    for i in range(1):
        for j in range(1):
            if a[i][j]<a[i][j+1] and a[i][j]<a[i+1][j]:
                b.append(a[i][j])
    for i in range(1):
        for j in range(n-1,n):
            if a[i][j]<a[i][j-1] and a[i][j]<a[i+1][j]:
                b.append(a[i][j])
    for i in range(n-1,n):
        for j in range(1):
            if a[i][j]<a[i][j+1] and a[i][j]<a[i-1][j]:
                b.append(a[i][j])
    for i in range(n-1,n):
        for j in range(n-1,n):
            if a[i][j]<a[i][j-1] and a[i][j]<a[i-1][j]:
                b.append(a[i][j])
    return b
import random
n = int(input('Розмірність:'))
a = [[random.randrange(0,10)for i in range(n)]for j in range(n)]
for i in range(n):
    print(a[i])
print('===================')
call = len(local())
print('Кількість локальних мінімумів даної матриці:'+str(call))
