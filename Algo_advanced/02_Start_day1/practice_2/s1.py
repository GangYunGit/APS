import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input()) + 1):
    arr = input().lower()                   # 16진수로 인식시키기 위해 소문자로 바꾸어준다.
    bin_code = ''                           # 2진수로 변환된 수를 저장

    # 입력된 16진수를 10진수로 바꾸는 과정
    for hex_num in arr:
        dec_num = int(hex_num, base=16)     # int의 base 옵션을 이용하여 16진수를 10진수로 변환

        # 10진수를 2진수로 바꾸는 과정
        for i in range(3, -1, -1):          # MSB 부터 검사
            if dec_num & (1 << i):          # ex) dec_num = 13(2진수로 1101)일 때 2^3번째 비트 값 = 1 이므로
                bin_code += '1'             # bin_code에는 '1'이 추가됨
            else:                           # ex) dec_num = 13(2진수로 1101)일 때 2^1번째 비트 값 = 0 이므로
                bin_code += '0'             # bin_code에는 '0'이 추가됨

    result = []

    # bin_code를 7개씩 나누어줌
    for i in range(0, len(bin_code), 7):
        # 2진수를 다시 int의 base옵션을 활용하여 10진수로 변환 후 result에 append
        result.append(int(bin_code[i:i + 7:], base=2))

    print(*result)
