class Streight:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C
    def rivn(self):
        return '{0}x+{1}y+{2}=0'.format(self.A,self.B,self.C)
    def __getitem__(self,key):
        if key==0:
            return self.A
        elif key==1:
            return self.B
        elif key==2:
            return self.C
        else:
            raise KeyError('Неправильний індекс')
    def __setitem__(self,key,value):
        if key==0:
            self.A=value
        elif key==1:
            self.B=value
        elif key==2:
            self.C=value
        else:
            raise KeyError('Неправильний індекс')
    def nalezh(self):
        x = int(input('Координати точки,x:'))
        y = int(input('Координати точки,y:'))
        if y==(-self.A*x-self.C)/self.B:
            print('Точка належить даній прямій')
        else:
            print('Точка не належить даній прямій')
    def peretin(self):
        koefA = int(input('Коефіціент при А:'))
        koefB = int(input('Коефіціент при B:'))
        koefC = int(input('Коефіціент при C:'))
        print('Вихідне рівняння прямої: {0}x+{1}y+{2}=0'.format(koefA,koefB,koefC))
        x = (-self.B*(koefA*self.C-self.A*koefC)/(self.A*koefB-koefA*self.B)-self.C)/self.A
        y = (koefA*self.C-self.A*koefC)/(self.A*koefB-koefA*self.B)
        return x,y

call = Streight(2,5,4)
m1 = call.rivn()
print('Рівняння прямої на площині: {0}'.format(m1))
call.nalezh()
m2 = call.peretin()
print('Точка перетину двох прямих:M{0}'.format(m2))
