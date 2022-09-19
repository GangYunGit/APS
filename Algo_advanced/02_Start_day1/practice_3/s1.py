import sys
sys.stdin = open('input.txt')

# 문제에서 주어진 암호 비트 패턴
bit_pattern = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9,
}

for test_case in range(1, int(input()) + 1):
    arr = input().lower()       # 16진수 계산을 위해 대문자를 소문자로 바꾸어줌
    bin_code = ''

    # 입력 받은 16진수 배열에 대하여 10진수로 변환한 후 다시 2진수로 변환
    for hex_num in arr:
        # 0의 개수가 부족하면 왼쪽부터 붙이기 위해 배열을 거꾸로 놓고 저장
        bin_num = bin(int(hex_num, base=16))[2::][::-1]
        while len(bin_num) != 4:
            bin_num += '0'
        bin_code += bin_num[::-1]      # 다시 원상복구하여 네자리의 2진수를 만들어줌

    result = []
    for i in range(len(bin_code) - 1, -1, -1):                       # bin_code 배열을 거꾸로 돌면서
        if bin_code[i] == '1':                                       # '1'을 찾았다면
            for j in range(0, len(bin_code), 6):                     # 찾은 부분부터 6개씩
                sliced_bin_code = bin_code[i - 5 - j:i + 1 - j:]     # 잘라서 새로운 변수에 대입
                if sliced_bin_code in bit_pattern.keys():            # 그 변수가 암호 패턴의 key와 일치하면
                    result.append(bit_pattern[sliced_bin_code])      # 결과에 저장
            break

    print(*result[::-1])        # 결과를 거꾸로 출력