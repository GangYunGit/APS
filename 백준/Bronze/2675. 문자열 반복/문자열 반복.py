n = int(input())
for _ in range(n):
    num, word = input().split()
    for i in range(len(word)):
        for j in range(int(num)):
            print(word[i], end="")
    print()