# List Parameters Example
def countOdds(a):
    count = 0
    for item in a:
        if (item % 2 == 1):
            count += 1
    return count

print(countOdds([2, 3, 7, 8, 21, 23, 24]))

# Modifying list elements is visible to caller: fill(list, value)
def fill(a, value):
    for i in range(len(a)):
        a[i] = value

a = [1, 2, 3, 4, 5]
print("At first, a =", a)
fill(a, 42)
print("After fill(a, 42), a =", a)

# List Return Types
def numbersWith3s(lo, hi):
    result = [ ]
    for x in range(lo, hi):
        if ("3" in str(x)):
            result.append(x)
    return result

print(numbersWith3s(250, 310))
