import sys
sys.stdin = open('input.txt', encoding='utf-8')


def bfs(v):
    global count
    count += 1
    visited[v] = True
    queue.append(v)
    temp = [v]
    contact.append(temp)

    while queue:
        t = queue.pop(0)
        temp = []
        for next_t in adj_list[t]:
            if not visited[next_t]:
                count += 1
                visited[next_t] = True
                queue.append(next_t)
                temp.append(next_t)
            print(len(queue))
        if temp:
            contact.append(temp)

        print()


for test_case in range(1, 11):
    vertex_num, start = map(int, input().split())
    vertex = list(map(int, input().split()))
    adj_list = [[] for _ in range(101)]

    for i in range(0, vertex_num, 2):
        adj_list[vertex[i]].append(vertex[i + 1])

    visited = [False] * 101
    queue = []
    contact = []
    count = 0
    bfs(start)
    # print(contact)
    print(adj_list)
    print(contact)
    print()

