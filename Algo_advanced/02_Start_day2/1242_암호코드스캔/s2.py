def ternary(n):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)

    return rev_base[::-1]


ternary_num = int('112', base=3)

print(ternary_num)

for i in range(3):
    j = 3 ** i
    if int(ternary(ternary_num)) && j == 2:
        print(2, end=' ')
    elif int(ternary(ternary_num)) && j == 1:
        print(1, end=' ')
    else:
        print(0, end=' ')
