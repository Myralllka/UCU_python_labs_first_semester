n = int(input())
numbers = list(map(float, input().strip().split()))
count = 0
for each in numbers:
    if(each) < 30:
        count += 1
milk = count * 200
pack = milk // 900
if milk % 900 != 0:
    pack = (milk // 900) + 1

print(pack, count)
