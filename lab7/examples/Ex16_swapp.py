a = [ 2, 3, 5, 7 ]
print("a =", a)

# Failed swap
a[0] = a[1]
a[1] = a[0]
print("After failed swap of a[0] and a[1]:")
print("   a=",a)

a = [ 2, 3, 5, 7 ]
print("a =", a)

# Swap with a temp variable
temp = a[0]
a[0] = a[1]
a[1] = temp
print("After swapping a[0] and a[1]:")
print("   a=",a)

# Swap with parallel (tuple) assignment
a[0],a[1] = a[1],a[0]
print("After swapping a[0] and a[1]:")
print("   a=",a)
