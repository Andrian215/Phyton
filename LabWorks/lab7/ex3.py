import random
N = int(input('N='))
matrix = [[random.randint(0,10)for x in range(N)]for y in range(N)]
for x in range(len(matrix)):
        print(matrix[x])
print('--------------------------------------')
a = matrix
for x in range(0,N-1):
    for y in range(x,N-1):
        d=a[y][x]/a[x][x]
        for i in range(x+1,N):
            a[y][i]=a[y][i]-d*a[y][i]
        for el in range(1):
            a[y][0]=a[y][0]-d*a[y][i]
        for els in range(1):
            a[0][0]=a[0][0]-d*a[y][i]
for i in range(N):
    print(a[i])
