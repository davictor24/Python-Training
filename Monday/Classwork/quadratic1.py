a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = b*b - 4*a*c

if D > 0:
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    print("x1 = {0}\nx2 = {1}".format(x1, x2))

elif D == 0:
    x = -b / (2*a)
    print("x = {0} (twice)".format(x))
    
else:
    re = -b / (2*a)
    im = ((-D)**0.5) / (2*a)
    print("x1 = {0} + j{1}\nx2 = {0} - j{1}".format(re, im))
