var1, var2 = int(input()), int(input())
for each in range(var1):
    if each == var1 - 1 or each == 0:
        print("*" * var2)
    else:
        print("*", " " * (var2 - 4), "*", sep='/')
