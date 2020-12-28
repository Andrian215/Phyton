class TEquation:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def lequation(self):
        return
    def qequation(self):
        return
    def finding_roots_of_equation(self):
        return
    def root_check(self):
        return
class LinearEquation(TEquation):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
    @property
    def lequation(self):
        return '{0}x={1}'.format(self.a,self.b)
    def finding_roots_of_equation(self):
         if self.a!=0:
             x=self.b / self.a
             return x
         elif self.a==0 and self.b!=0:
             x = 'Коренів немає'
             return x
         elif self.a==0 and self.b==0:
             x = 'Безліч коренів'
             return x
    def root_check(self):
        global x
        Root=float(input('Введіть значення:'))
        if self.a != 0:
            x = self.b / self.a
        elif self.a == 0 and self.b != 0:
            x = None
        elif self.a == 0 and self.b == 0:
            x = 0
        if Root==x:
            v = 'Дане значення є коренем лінійного рівняння'
        else:
            v = 'Дане значення не є коренем лінійного рівняння'
        return v
class QuadraticEquation(TEquation):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
    @property
    def qequation(self):
        return '{0}x^2+{1}x+{2}=0'.format(self.a,self.b,self.c)
    def finding_roots_of_equation(self):
        if self.b==0 and self.c!=0:
            if -self.c/self.a>0:
                x=(-self.c/self.a)**0.5,-(-self.c/self.a)**0.5
                return x
        elif self.c==0 and self.b!=0:
            x=0,-self.b/self.a
            return x
        elif self.b==0 and self.c==0:
            x=0
            return x
        elif self.a!=0 and self.b!=0 and self.c!=0:
            D=self.b**2-4*self.a*self.c
            x = (-self.b-D**0.5)/(2*self.a), (-self.b+D**0.5)/(2*self.a)
            return x
    def root_check(self):
        global x,v
        if self.b==0 and self.c!=0:
            if -self.c/self.a>0:
                x=(-self.c/self.a)**0.5,-(-self.c/self.a)**0.5
        elif self.c==0 and self.b!=0:
            x=0,-self.b/self.a
        elif self.b==0 and self.c==0:
            x=0
        elif self.a!=0 and self.b!=0 and self.c!=0:
            D=self.b**2-4*self.a*self.c
            x = (-self.b-D**0.5)/2*self.a,(-self.b+D**2)/2*self.a
        Root= float(input('Введіть значення:'))
        for i in range(len(x)):
            if Root==x[i]:
                v = 'Дане значення є коренем квадратного рівняння'
            else:
                v = 'Дане значення не є коренем квадратного рівняння'
        return v
    def sum_of_roots(self):
        global x
        if self.b == 0 and self.c != 0:
            if -self.c / self.a > 0:
                x = ((-self.c / self.a) ** 0.5) + (-(-self.c / self.a) ** 0.5)
        elif self.c == 0 and self.b != 0:
            x =-self.b / self.a
        elif self.b == 0 and self.c == 0:
            x = 0
        elif self.a != 0 and self.b != 0 and self.c != 0:
            D = self.b ** 2 - 4 * self.a * self.c
            x = ((-self.b - D ** 0.5)/2*self.a) + ((-self.b + D ** 2) / 2 * self.a)
        return x
import random
call = LinearEquation(random.randint(-10,10),random.randint(-10,10),0)
Call = QuadraticEquation(random.randint(-10,10),random.randint(-10,10),random.randint(-10,10))
m1 = call.lequation
m2 = call.finding_roots_of_equation()
m3 = call.root_check()
m4 = Call.qequation
m5 = Call.finding_roots_of_equation()
m6 = Call.root_check()
m7 = Call.sum_of_roots()
print('Рівняння має вигляд:{0}\nЙого корінь:{1}'.format(m1,m2))
print(m3)
print('Квадратне рівняння має вигляд:{0}\nКорені цього рівняння:{1}'.format(m4,m5))
print(m6)
print('Сума коренів квадратного рівняння:{0}'.format(m7))
