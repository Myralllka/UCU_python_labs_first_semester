import copy

# Modifying list reference is not visible to caller
def destructiveRemoveAll(a, value):
    while (value in a):
        a.remove(value)

def nonDestructiveRemoveAll(a, value):
    a = copy.copy(a)
    while (value in a):
        a.remove(value)
    return a

a = [ 1, 2, 3, 4, 3, 2, 1 ]
print("At first")
print("   a =", a)

destructiveRemoveAll(a, 2)
print("After destructiveRemoveAll(a, 2)")
print("   a =", a)

b = nonDestructiveRemoveAll(a, 3)
print("After b = nonDestructiveRemoveAll(a, 3)")
print("   a =", a)
print("   b =", b)
