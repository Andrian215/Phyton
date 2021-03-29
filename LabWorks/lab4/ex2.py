a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

if a<=b and a<=c:
    print(a**2)
elif b<=a and b<=c:
    print(b**2)
elif c<=a and c<=b:
    print(c**2)
