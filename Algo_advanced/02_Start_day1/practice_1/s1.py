import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input()) + 1):
    arr = input()[::-1]                 # 계산을 왼쪽에서 하기 위해 배열을 뒤집어준다.
    decode_list = []                    # 십진수로 변환된 값들을 저장하기 위한 리스트

    # 7개의 byte를 묶어줌
    for i in range(0, len(arr), 7):
        decode = 0

        # 묶음을 하나씩 검사하며 10진수로 변환
        for j in range(7):
            decode += 2 ** j * int(arr[i + j])      # decode = 자릿수(2의 j제곱) * (비트가 1인지 0인지 검사한 값)
        decode_list.append(decode)                  # 리스트에 저장

    print(*decode_list[::-1])                       # 저장된 값을 거꾸로 출력
