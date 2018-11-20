import copy

# Create a list
a = [ 2, 3 ]

# Try to copy it
b = a             # Error!  Not a copy, but an alias
print (id(a), id(b))
c = copy.copy(a)  # Ok
print (id(a), id(c))

# At first, things seem ok
print("At first...")
print("   a =", a)
print("   b =", b)
print("   c =", c)

# Now modify a[0]
a[0] = 2015
print("But after a[0] = 2015")
print("   a =", a)
print("   b =", b)
print("   c =", c)

from copy import deepcopy

lst1 = ['a','b',['ab','ba']]

lst2 = copy.copy(lst1)

lst2[2][1] = "d"
lst2[0] = "c";

print (lst2)
print (lst1)
