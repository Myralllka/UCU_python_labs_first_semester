# Add an item with list1 + list2
a = [ 2, 3, 6, 7, 14 ]
b = a + [ 13, 17 ]
print(a)
print(b)

# Insert an item at a given index
c = a[3:]
b = a[:2] + [5] + c
print(c) 
print(a)
print(b)

# Destructive vs Non-Destructive
print("Destructive:")
a = [ 2, 3 ]
b = a
a += [ 4 ]
print(a)
print(b)

print("Non-Destructive:")
a = [ 2, 3 ]
b = a
a = a + [ 4 ]
print(a)
print(b)
