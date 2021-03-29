import random
N = int(input('N='))
matrix = [[random.randrange(-10,10)for x in range(N)]for y in range(N)]
for el in range(N):
    print(matrix[el])
print('----------------')
a = [matrix[el][el]for el in range(N)]
a.sort(reverse=True)
for el in range(N):
    matrix[el][el]=a[el]
for el in range(N):
    if True:
        print(matrix[el])
