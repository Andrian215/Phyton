def rec(i):
    if i == 0:
        return 1
    if i == 1 or i == 2 or i == 3:
        return 7
    else:
        xn=(rec(i-1)*(1+rec(i-2))+rec(i-3))/rec(i-4)
        return xn
n = int(input('n='))
print(rec(n))
