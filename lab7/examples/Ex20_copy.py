import copy

a = [2, 3]
b = copy.copy(a)
c = a[:]
d = a + [ ]
e = list(a)
f = copy.deepcopy(a)
g = sorted(a)

a[0] = 42
b[0] = 2015
print(a, b, c, d, e, f, g)

lst1 = ['a','b',['ab','ba']]
lst2 = copy.copy(lst1)

lst2[2][1] = "d"
lst2[0] = "c"

print (lst2)
print (lst1)

lst1 = ['a','b',['ab','ba']]
lst3 = copy.deepcopy(lst1)

lst3[2][1] = "D"
lst3[0] = "C"

print (lst3)
print (lst1)




