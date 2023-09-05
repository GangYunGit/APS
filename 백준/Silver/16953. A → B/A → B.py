a, b = input().split()

count = 0
while True:
    if int(b) == int(a):
        break
    elif int(b) < int(a):
        count = -2
        break

    if int(b) % 2:
        if b[-1] == '1':
            b = b[:len(b) - 1]
            count += 1
        else:
            count = -2
            break
    else:
        b = str(int(b) // 2)
        count += 1
print(count + 1)