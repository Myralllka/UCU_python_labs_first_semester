a = [ 2, 3, 4, 5, 6, 7, 8 ]

# Remove an item with slice assignment
a[2:4] = [ ]
print("a =", a)

# Remove an item with the del operator
del a[2:4]
print("a =", a)

# Remove an item at a given index (with list slices)
b = a[:2] + a[3:]
print("After b = a[:2] + a[3:]")
print("   a =", a)
print("   b =", b)

