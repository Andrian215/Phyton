import random

class TSMatrix:
    def __init__(self,elements,n):
        self.n=n
        self.elements=elements
    def returnelements(self):
        return self.elements
    def min_max_elements(self):
        maxmin=[self.elements[i][j] for i in range(n) for j in range(n)]
        return max(maxmin),min(maxmin)
    def sum_of_elements(self):
        twoarraysintoone = [self.elements[i][j]for i in range(n)for j in range(n)]
        for i in range(n):
            return sum(twoarraysintoone)
    def __add__(self,other):
        s = [[self.elements[j][i]+other.elements[j][i] for i in range(n)] for j in range(n)]
        return s
    def __sub__(self,other):
        s = [[self.elements[i][j]-other.elements[i][j] for i in range(n)] for j in range(n)]
        return s
n = int(input('n='))
els = [[random.randrange(-10,10)for i in range(n)]for j in range(n)]
ttt = TSMatrix(els,n)
m1 = ttt.returnelements()
m2 = ttt.min_max_elements()
m3 = ttt.sum_of_elements()
F1 = TSMatrix([[2,4,1],[6,5,2],[4,3,1]],n)
F2 = TSMatrix([[2,4,1],[6,5,2],[4,3,1]],n)
print('Матриця розмірності {0}x{0}:{1}\n(макс.ел,мін.ел)={2}\nСума елементів відповідно={3}'.format(n,m1,m2,m3))
print('Сума елементів двох матриць:{0}'.format(F1+F2))
print('Різниця елементів двох матриць:{0}'.format(F1-F2))
