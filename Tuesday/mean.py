n = int(input("Enter n: "))
l = []
for i in range(n):
    l.append(float(input("Enter data {0}: ".format(i+1))))
total = 0
for i in range(n):
    total += l[i]
mean = total / n
print("Mean = {0}".format(mean))
