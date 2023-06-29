n1, n2 = int(input()), int(input())
for num in str(n2)[::-1]:
    print(n1 * int(num))
print(n1 * n2)