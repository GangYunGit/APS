T = int(input())

for test_case in range(1, T + 1):  # 테스트 케이스
    width = int(input())  # 방의 넓이(박스의 총 개수)
    boxes = list(map(int, input().split()))  # 박스의 높이를 담은 배열
    result = 0  # 결과를 출력할 변수

    for i in range(width):  # 박스의 총 개수만큼 수행
        drop = 0  # 박스별 떨어진 높이(초기화 시점에 주의)
        for j in range(width - i):  # i번째 박스 오른쪽의 모든 박스들과 비교
            if boxes[i] > boxes[i + j]:  # i번째 박스가 더 길 때만 낙하 가능
                drop += 1
        if drop > result:
            result = drop  # 가장 큰 drop값을 result에 저장

    print(f'#{test_case} {result}')
