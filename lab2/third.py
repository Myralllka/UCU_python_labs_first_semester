import math
value = eval(input())
v = round(((value ** 3) * 4 * math.pi / 3), 3)
a = round(((value ** 2) * 4 * math.pi), 3)
if v == int(v):
    v = int(v)
if a == int(a):
    a = int(a)
print("V = ", v)
print("A = ", a)
