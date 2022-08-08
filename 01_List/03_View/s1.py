for test_case in range(1, 11):  # 10개의 테스트 케이스
    width = int(input())  # 가로 길이
    bds = list(map(int, input().split()))  # 빌딩의 높이들을 배열에 저장
    you_can_see = 0  # 조망이 확보되는 세대의 개수

    for i in range(width):
        if i >= 2 or i <= (width - 3):  # 양쪽 끝 2칸은 제외하고 반복문 수행
            # i 번째 빌딩의 양쪽 2방향이 비어있는지 확인
            if (
                bds[i] > bds[i - 2]
                and bds[i] > bds[i - 1]
                and bds[i] > bds[i + 2]
                and bds[i] > bds[i + 1]
            ):
                # 양쪽 2방향의 빌딩 중 조망을 가장 많이 가리는 빌딩의 높이를 빼줌
                you_can_see += bds[i] - max(
                    bds[i - 2], bds[i - 1], bds[i + 1], bds[i + 2]
                )

    print(f'#{test_case} {you_can_see}')
