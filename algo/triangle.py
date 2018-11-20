num = sorted(list(map(int, input().strip().split())))
print(num)
if ((num[3] < num[2] + num[1]) or (num[2] < num[1] + num[0])):
    print("TRIANGLE")
elif ((num[3] == num[2] + num[1]) or (num[2] == num[1] + num[0])):
    print("SEGMENT")
else:
    print("IMPOSSIBLE")
