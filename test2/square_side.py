def input_std():
    a, b, c, e = list(map(int,
                          input("print here a, b, c, e  ").strip().split()))
    return a, b, c, e


def input_f(path):
    with open(path, "r", encoding='utf-8') as inp:
        result = inp.readline()
    return result


def r_triangle_sqr(a, b):
    return a * b / 2


def triangle_sqr(a, b):
    b = b / 2
    c = pow(a**2 - b**2, .5)
    return (b * c // 2)


def quadr_sqr(a):
    return a**2


def main():
    a, b, c, e = input_std()
    if a == b:
        dec, eq = c, a
    elif a == c:
        dec, eq = b, a
    else:
        dec, eq = a, b
    # for i in range(dec // 2 - 1, dec, e):


print(input_f())
