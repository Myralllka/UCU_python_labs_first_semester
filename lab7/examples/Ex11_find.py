a = [ 2, 3, 5, 2, 6, 2, 2, 7 ]

print("a            =", a)
print("a.index(6)   =", a.index(6))
print("a.index(2)   =", a.index(2))
print("a.index(2,1) =", a.index(2,1))
print("a.index(2,4) =", a.index(2,4))

# crashes when item is not in list
print("a.index(9) =", a.index(9)) # crashes!
#print("This line will not run!")

if (9 in a):
    print("a.index(9) =", a.index(9))
else:
    print("9 not in", a)
print("This line will run now!")
