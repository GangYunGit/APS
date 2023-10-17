n = int(input())
check = 1
row = 0
for i in range(1, 4500):
    row += i
    check += 1
    if row >= n:
        row -= i
        break
idx = n - row
if check % 2:
    print(f'{idx}/{check - idx}')
else:
    print(f'{check - idx}/{idx}')