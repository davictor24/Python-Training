def fact(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fact(x - 1)

n = int(input("Enter n: "))
print("{0}! = {1}".format(n, fact(n)))
