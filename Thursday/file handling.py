file1 = open('OurFirstFile.txt','w')

for x in range(1,1000,2):
    y = str(x) + '\n'
    file1.write(y)
file1.close()


fileread = open('OurFirstFile.txt', 'r')

for x in fileread:
    print (x)

fileread.close()
