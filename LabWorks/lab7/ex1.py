import random
N = int(input('Кількість стовпців:'))
M = int(input('Кількість рядків:'))
matrix = [[random.randrange(-10,10)for x in range(N)]for y in range(M)]
a = [matrix[x]for x in range(N) if x%2==0]
b = [matrix[x][y]for x in range(M)for y in range(N) if y%2==1]
els1 = [a[i][j]for i in range(len(a))for j in range(N) if a[i][j]>=0]
els2 = [b[i]for i in range(len(b)) if b[i]>=0 and b[i] not in els1]
els = els1+els2
print(matrix)
print(len(els))
