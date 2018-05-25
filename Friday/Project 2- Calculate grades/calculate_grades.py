def get_grade(score):
    if score < 0 or score > 100:
        return "-"
    elif score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"

f1 = open("scores.txt", "r")
f2 = open("grades.txt", "w")

print("Computing....")
for line in f1:
    ln = line.strip("\n")
    f2.write(ln)
    arr = ln.split(",")
    gr = get_grade(int(arr[2]))
    f2.write("," + gr + "\n")
print("Done!")

f1.close()
f2.close()
print("Files closed.")
    
