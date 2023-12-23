for _ in range(int(input())):
    num = list(map(int, input().split()))
    even = []
    for i in range(7):
        if num[i] % 2 == 0:
            even.append(num[i])
    print(sum(even), min(even))