import sys


N = 8


def encode(i, j):
    return i * N + j


def decode(numm):
    i = numm // N
    j = numm % N
    return(i, j)


di = [-1, -2, -2, -1, 1, 2, 2, 1]
dj = [-2, -1, 1, 2, 2, 1, -1, -2]


def valid(i, j):
    return i >= 0 and i < N and j >= 0 and j < N


def neighbors(numm):
    res = []
    i, j = decode(numm)
    for q in range(8):
        ni = i + di[q]
        nj = j + dj[q]
        if valid(ni, nj):
            res.append(encode(ni, nj))
    return res


d = [[float("inf")] * (N**2) for i in range(N**2)]
for i in range(N**2):
    d[i][i] = 0


for i in range(N**2):
    for to in neighbors(i):
        d[i][to] = 1

for k in range(N**2):
    for i in range(N**2):
        for j in range(N**2):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])


def solve(line):
    a, b = line.split()
    aj = ord(a[0]) - ord('a')
    bj = ord(b[0]) - ord('a')
    ai = N - int(a[1])
    bi = N - int(b[1])

    ac = encode(ai, aj)
    bc = encode(bi, bj)

    res = d[ac][bc]

    print("To get from %s to %s takes %s knight moves." % (a, b, res))


for line in sys.stdin:
    solve(line)
