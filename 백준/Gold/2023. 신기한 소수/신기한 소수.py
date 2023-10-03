def prime_check(num):
    check = int(num)
    for i in range(2, int(check ** 0.5) + 1):
        if check % i == 0:
            return
    else:
        if len(num) == n:
            print(num)
            return

        for j in end_number:
            prime_check(num + j)


n = int(input())
end_number = ['1', '3', '7', '9']
for i in ['2', '3', '5', '7']:
    prime_check(i)