def myrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in myrange(10):
    print(i)
