from math import pi

class TCircle:
    def __init__(self,r,centrex,centrey,centrez):
        self.r=r
        self.centrex=centrex
        self.centrey=centrey
        self.centrez=centrez
    def return_r_and_centre(self):
        return self.r,(self.centrex,self.centrey)
    def square(self):
        return self.r*self.r*pi
    def func(self):
        x = int(input('Довільна точка, координата x='))
        y = int(input('Довільна точка, координата y='))
        moduleofpoint=((x-self.centrex)**2+(y-self.centrey)**2)**0.5
        if moduleofpoint>=self.r:
            print('Точка не належить даному колу')
        else:
            print('Точка належить даному колу')
    def __sub__(self,other):
        return self.r-other.r
    def __add__(self,other):
        return self.r+other.r
    def __rmul__(self,other):
        return self.r*other
class TBall(TCircle):
    def __init__(self,_r,_centrex,_centrey,_centrez):
        super().__init__(_r,_centrex,_centrey,_centrez)
    def volume_of_ball(self):
        return 4/3*pi*self.r
    def return_r_and_centre(self):
        return self.r,(self.centrex,self.centrey,self.centrez)
    def square(self):
        return 4*self.r*self.r*pi
    def func(self):
        x = int(input('Довільна точка, координата х:'))
        y = int(input('Довільна точка, координата y:'))
        z = int(input('Довільна точка, координата z:'))
        moduleofpoint = ((x-self.centrex)**2+(y-self.centrey)**2+(z-self.centrez)**2)**0.5
        if moduleofpoint>=self.r:
            print('Точка не належить даній сфері')
        else:
            print('Точка належить даній сфері')
    def __add__(self,other):
        return self.r+other.r
    def __sub__(self,other):
        return self.r-other.r
    def __rmul__(self,other):
        return self.r*other
print('For Circle:')
r1 = int(input('Радіус першого кола='))
r2 = int(input('Радіус другого кола='))
if r1<0 or r2<0:
    del r1,r2
    print("Радіус не може бути відє'мний!")
call1 = TCircle(r1,2,1,3)
m2=call1.square()
call2 = TCircle(r2,2,1,3)
call1.func()
print('Площа  кола={0}'.format(m2))
print('Різниця радіусів:{0}'.format(call1-call2))
print('Сума радіусів:{0}'.format(call1+call2))
m3 = call1.__rmul__(5)
print('Радіус помножений на число={0}'.format(m3))
print('For Ball:')
call_ball1 = TBall(r1,2,1,3)
call_ball2 = TBall(r2,2,1,3)
call_ball1.func()
met2 = call_ball1.square()
met3 = call_ball1.volume_of_ball()
print('Сума радіусів сфер:{0}'.format(call_ball1+call_ball2))
print('Різниця радіусів сфер:{0}'.format(call_ball1-call_ball2))
met = call_ball1.__rmul__(10)
print('Радіус сфери помножений на число:{0}'.format(met))
print("Площа сфери={0}, Об'єм кулі={1}".format(met2,met3))
