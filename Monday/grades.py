grade = int(input("Enter grade (0 - 100): "))

if grade < 0 or grade > 100:
    print("Invalid grade!")
else:
    if grade >= 70:
        print("A")
    elif grade >= 60:
        print("B")
    elif grade >= 50:
        print("C")
    elif grade >= 45:
        print("D")
    elif grade >= 40:
        print("E")
    else:
        print("F")
        
