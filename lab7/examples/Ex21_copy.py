# Destructively with list.sort()
a = [ 7, 2, 5, 3, 5, 11, 7 ]
print("At first, a =", a)
a.sort()
print("After a.sort(), a =",a)

# Non-Destructively with sorted(list)
a = [ 7, 2, 5, 3, 5, 11, 7 ]
print("At first")
print("   a =", a)
b = sorted(a)
print("After b = sorted(a)")
print("   a =", a)
print("   b =", b)

# Sorting with a key function
a = [ 10, 2, -5, 8, -3, 7, 1 ]
print(sorted(a))
print(sorted(a, key=abs))
