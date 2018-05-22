var1 = float(input('Enter the first number: '))
var2 = float(input('Enter the second number: '))


print('Enter the operation you want to perform: \n')
print('1: Addition \n')
print('2: Subtraction \n')
print('3: Multiplication \n')
print('4: Division \n')
print('5: Modulo \n')
print('6: Determine the larger number \n')
print('7: Division of the larger number by the smaller number \n')

choice = input('Your Operation: ')      #choice here is a string
int_choice= int(choice)     #Converts choice from string to integer

if int_choice == 1:
    var3 = var1 + var2
    print('The sum of the two numbers is: ', var3)
elif int_choice == 2:
    var3 = var1 - var2
    print('The difference of the two numbers is: ', var3)
elif int_choice == 3:
    var3 = var1 * var2
    print('The product of the two numbers is: ', var3)
elif int_choice == 4:
    var3 = var1 / var2
    print('The quotient of the two numbers is: ', var3)
elif int_choice == 5:
    var3 = var1 % var2
    print('The modulo of the two numbers is: ', var3)
elif int_choice == 6:
    if var1 > var2:
        print('The larger number is: ',var1)
    else:
        print('The larger number is: ',var2)
elif int_choice == 7:
    if var1 > var2:
        var3 = var1 / var2
        print('The larger number divided by the smaller number is: ',var3)
    else:
        var3 = var2 / var1
        print('The larger number divided by the smaller number is: ',var3)
else:
    print('Invalid Selection')

