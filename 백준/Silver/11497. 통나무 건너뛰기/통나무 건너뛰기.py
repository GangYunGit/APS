for test_case in range(int(input())):
    N = int(input())
    li = list(map(int, input().split()))
    li.sort()
    new_li = li[0:N:2] + li[1:N:2][::-1]
    max_difficulty = 0
    for i in range(len(new_li)):
        max_difficulty = max(abs(new_li[i - 1] - new_li[i]), max_difficulty)
    print(max_difficulty)