  
class Pod:
    def __init__(self,_a):
        self.a=_a
    def adding_digit(self):
        return self.a.append(random.randint(-10,10))
    def return_digit(self):
        return self.a
    def max_in_digits(self):
        return max(list(self.a))
    def sum_of_digits(self):
        return sum(list(self.a))
import random
digit = Pod([random.randint(-10,10) for el in range(10)])
print(digit.a)
b = digit.return_digit()
mx = digit.max_in_digits()
suma = digit.sum_of_digits()
adding = digit.adding_digit()
print('Цифри,які входять у множину={0}; Сума усіх цифр множини={1}; Найбільший елемент={2}'  .format(b,suma,mx))
