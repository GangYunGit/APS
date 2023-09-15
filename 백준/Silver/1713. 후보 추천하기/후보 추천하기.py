def update_photo(student_id, time):
    for i in range(len(photo)):
        if photo[i][2] == student_id:
            photo[i][0] += 1
            break
    else:
        if len(photo) >= n:
            photo.pop()
        photo.append([1, time, student_id])
    photo.sort(reverse=True)


n = int(input())
likes = int(input())
likes_list = list(map(int, input().split()))
photo = []
result = []
for i in range(likes):
    update_photo(likes_list[i], i)

for i in range(len(photo)):
    result.append(photo[i][2])

print(*sorted(result))