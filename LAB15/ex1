def fordynamic(elements):
    n = 0
    while n != 111:
        n = int(input('Додати елемент, якщо непотрібно введіть 111='))
        elements.append(n)
        if 111 in elements:
            elements.remove(111)
        print(elements)
    while n != 333:
        n = int(input('Видалити елемент,якщо не потрібно введіть 333='))
        if n in elements:
            elements.remove(n)
            print(elements)
        elif n != 333 and n not in elements:
            print('Такого елемента немає')
            print(elements)
    return elements

class Array:
    def __init__(self,elements):
        self.elements=elements
    def returarray(self):
        return self.elements
    def sum(self):
        return
    def product(self):
        return
    def sa(self):
        return
class ArraY(Array):
    def __int__(self,_elements):
        super().__init__(_elements)
    def sum(self):
        return sum(self.elements)
    def product(self):
        d=1
        for i in range(len(self.elements)):
            d*=self.elements[i]
        return d
    def sa(self):
        return sum(self.elements)/len(self.elements)

masiv = list(map(int,input().split()))
m4 = fordynamic(masiv)
call = ArraY(m4)
m1 = call.sum()
m2 = call.product()
m3 = call.sa()
print(m4)
print(m1,m2,m3)
print()
