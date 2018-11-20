a = [ 2, 3, 5, 3, 7, 6, 5, 11, 13 ]
print("a =", a)

# Remove an item with list.remove(item)
a.remove(5)
print("After a.remove(5), a=", a)

a.remove(5)
print("After another a.remove(5), a=", a)

# Remove an item at a given index with list.pop(index)
item = a.pop(3)
print("After item = a.pop(3)")
print("   item =", item)
print("   a =", a)

item = a.pop(3)
print("After another item = a.pop(3)")
print("   item =", item)
print("   a =", a)

# Remove last item with list.pop()
item = a.pop()
print("After item = a.pop()")
print("   item =", item)
print("   a =", a)
