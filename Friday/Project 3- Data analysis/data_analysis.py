import random

def random_array(minimum, maximum, n):
    arr = []
    for i in range(n):
        arr.append(random.randint(minimum, maximum))
    return arr

def mean(arr):
    return sum(arr) / len(arr)

def median(arr):
    sorted_array = sorted(arr)
    n = len(arr)
    if n % 2 == 1:
        return sorted_array[int(n / 2)]
    else:
        return (sorted_array[int(n/2) - 1] + sorted_array[int(n/2)]) / 2

def mode(arr):
    d = {}
    for num in arr:
        d[num] = d[num] + 1 if num in d else 1
    mode_arr = [key for key in d.keys() if d[key] == max(d.values())]
    return mode_arr[0] if len(mode_arr) == 1 else mode_arr

def variance(arr):
    m = mean(arr)
    dev_squared = [(x - m)**2 for x in arr]
    return sum(dev_squared) / len(arr)

def standard_dev(arr):
    return variance(arr) ** 0.5

def check_normality(arr):
    m = mean(arr)
    s = standard_dev(arr)
    left = m - s
    right = m + s
    count = 0
    for item in arr:
        if left <= item <= right:
            count += 1
    percent = (count / len(arr)) * 100
    print(str(percent) + "% of the data falls within m + s and m - s")


print("Computing...")
arr = random_array(1, 100, 1000000)
print("Mean = " + str(mean(arr)))
print("Median = " + str(median(arr)))
print("Mode = " + str(mode(arr)))
print("Variance = " + str(variance(arr)))
print("Standard deviation = " + str(standard_dev(arr)))
check_normality(arr)
print("Done!")
