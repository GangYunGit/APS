import sys
sys.stdin = open('input.txt', encoding='utf-8')


def in_order(n):
    global count
    if n:
        in_order(child_left[n])
        count += 1
        tree[n] = count
        in_order(child_right[n])


for test_case in range(1, int(input()) + 1):
    N = int(input())
    tree = list(range(N + 1))
    child_left = [0] * (N + 1)
    child_right = [0] * (N + 1)

    for i in range(1, N + 1):
        child_left[i] = i * 2
        child_right[i] = i * 2 + 1

    count = 0
    # in_order(1)
    print(tree)
    print(child_left)
    print(child_right)




