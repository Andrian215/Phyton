from math import factorial
ni = int(input('i = '))
nj = int(input('j = '))
a = [[factorial(i)-factorial(j) for j in range(1, nj+1)] for i in range(1, ni+1)]
s = [a[i][j] for i in range(ni) for j in range(nj) if (i+j)%2==1]
print(a)
print('Сума елементів з непарними індексами = {0}'.format(sum(s)))
