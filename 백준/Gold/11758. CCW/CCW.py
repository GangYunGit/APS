def func(a1, b1, a2, b2, a3, b3):
    cross_product = a1 * b2 + a2 * b3 + a3 * b1 - a2 * b1 - a3 * b2 - a1 * b3
    if cross_product > 0:
        return 1
    elif cross_product < 0:
        return -1
    else:
        return 0


p1, p2, p3 = [list(map(int, input().split())) for _ in range(3)]
print(func(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]))