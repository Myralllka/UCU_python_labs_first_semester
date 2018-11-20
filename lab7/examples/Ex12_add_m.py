# Add an item with list.append(item)
a = [ 2, 3 ]
a.append(7)
print(a)

# Add a list of items with list += list2
a += [' 11, 13 ']
print(a)

# Add a list of items with list.extend(list2)
a.extend([ 17, 19 ])
print(a)

# Insert an item at a given index
a.insert(2, 2015)  # at index 2, insert 2015
print(a)
