# Problem D
maxN = 10 ** 8

fibos = [1, 2]

while(True):
    curFibo = fibos[-1] + fibos[-2]
    if(curFibo > maxN):
        break
    fibos.append(curFibo)

fibos.reverse()

n = int(input())


def solve(m):
    minitial = m
    l = []
    was1 = False
    for fibo in fibos:
        if(fibo <= m):
            was1 = True
            l.append(1)
            m -= fibo
        else:
            if(was1):
                l.append(0)
    if(len(l) == 0):
        l.append(0)
    ans = str(minitial) + " = "
    ans += ''.join(list(map(str, l)))
    ans += " (fib)"
    print(ans)

for i in range(n):
    m = int(input())
    solve(m)
