import random

class TMatrix:
    def matrix(self):
        self.matrix=[[random.randrange(-11,11)for i in range(n)]for j in range(n)]
        matriX = [self.matrix[i] for i in range(n) for j in range(1) if self.matrix[i][j]==self.matrix[j][i]]
        if self.matrix==matriX:
            return self.matrix,':Матриця симетрична'
        try:
            for i in range(n):
                for j in range(n):
                    if self.matrix[i][j]!=self.matrix[i+1][j+1]:
                        return self.matrix
        except IndexError:
            print('Такого індекса в матриці немає')
        except self.matrix!=matriX:
            print('Матрця несеметрична')
        try:
            for i in range(n):
                for j in range(n):
                    if self.matrix[i][j]<=-10 or self.matrix[i][j]>=10:
                        print('Недопустиме значення')
        except Exception:
            print('Недопустиме значення')

n = int(input('Кількіть вимірів='))
call = TMatrix()
m1 = call.matrix()
print('Рандомна матриця={0}'.format(m1))
