def bessel(n, x):
    sigma = 0
    for m in range(0, 21):
        num = ((-1)**m) * (x**(2*m))
        den = (2**(2*m + n)) * fact(m) * fact(n + m)
        sigma += num / den
    return (x**n) * sigma

def fact(k):
    if k == 0 or k == 1:
        return 1
    else:
        f = 1
        for i in range(1, k + 1):
            f *= i
        return f
    
while True:
    n = int(input("n = "))
    x = float(input("x = "))
    print("Jn(x) = " + str(bessel(n, x)))
    print("Enter 'Y' to continue, enter anything else to quit")
    res = input("Your response: ")
    if res != "Y" and res != "y":
        break
