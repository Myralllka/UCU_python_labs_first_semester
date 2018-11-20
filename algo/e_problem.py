numbers = list(map(int, input().strip().split()))
n = numbers[2]
gr = numbers[0] * 100
cop = numbers[1]

summ = (gr + cop) * n
cop = summ % 100
gr = (summ - cop) // 100
print(gr, cop)
