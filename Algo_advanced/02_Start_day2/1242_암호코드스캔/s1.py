import sys
sys.stdin = open('input.txt', encoding='utf-8')

key = {13: 0, 25: 1, 19: 2, 61: 3, 35: 4, 49: 5, 47: 6, 59: 7, 55: 8, 11: 9}

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    video = [list(input().lower()) for _ in range(N)]

    scanner = []

    # 행은 정방향, 열은 역방향으로 순회하며 1을 처음으로 만나는 지점을 찾는다.
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if video[i][j] != '0':                      # 1을 찾았다면
                k = 0
                while video[i][j + k] != '0':                   # 그 부분부터 56개의
                    scanner.append(video[i][j + k])     # 비디오 정보를 scanner 에 append
                    k += 1
                break

    print(scanner)

    # decode_list = []
    #
    # for i in range(0, 56, 7):                       # 길이가 56인 비디오 정보를 7개씩 나누어서
    #     seven_bits = scanner[i:i + 7:]              # seven_bits 변수에 저장하고
    #     decode = 0                                  # 반복문을 돌면서 사용할 변수 초기화
    #     for j in range(7):                          # 7개의 길이만큼
    #         decode += 2 ** j * seven_bits[j]        # 10진수로 변환했을 때 나오는 수를 구한다
    #     decode_list.append(key[decode])             # 암호화 규칙에 맞추어 10진수를 변환하고 결과에 저장
    #
    # result = 0
    # for i in range(8):                              # 암호코드의 유효성 검사
    #     if i % 2:                                   # 홀수 자릿수이면
    #         result += decode_list[i] * 3            # 3을 곱해주고 결과에 저장
    #     else:                                       # 짝수 자릿수면
    #         result += decode_list[i]                # 그대로 더해주고 결과에 저장
    #
    # if result % 10:                                 # 결과가 10의 배수가 아니면
    #     result = 0                                  # 잘못된 암호이다
    # else:                                           # 결과가 10의 배수이면
    #     result = sum(decode_list)                   # 정답이다
    #
    # print(f'#{test_case} {result}')