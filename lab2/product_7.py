from math import factorial
number = eval(input())
result = factorial(number)
for each in range(7, number + 1, 7):
    result /= each
print(int(result))
