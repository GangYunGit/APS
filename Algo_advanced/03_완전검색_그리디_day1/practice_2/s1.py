# Baby-gin 검사

import sys
sys.stdin = open('input.txt')


# 베이비 진인지 확인해주는 함수
def is_baby_gin(deck):
    straight_count = 0
    triple_count = 0
    baby_gin_count = 0

    # 첫 번째 인덱스, 세 번째 인덱스를 시작점으로
    for i in range(0, 6, 3):
        if deck[i] + 2 == deck[i + 1] + 1 == deck[i + 2]:   # 연속된 숫자인지 판별
            straight_count += 1                             # 스트레이트

        if deck[i] == deck[i + 1] == deck[i + 2]:           # 똑같은 숫자인지 판별
            triple_count += 1                               # 트리플

    baby_gin_count += straight_count + triple_count         # 트리플과 스트레이트의 개수를 카운트

    if straight_count + triple_count == 2:                  # 카운트가 2개이면 babygin
        return True
    else:
        return False


# 순열을 이용하여 카드조합을 찾고, babygin인지 판별
def permutation(start, deck):
    cards_num = len(deck)
    if start == cards_num:                              # 순열을 완성했으면
        if is_baby_gin(deck):                           # 베이비 진인지 판별해봐
            deck_checker.append(True)                   # 맞으면 True
        else:
            deck_checker.append(False)                  # 아니면 False를 저장
        return

    # 순열을 만들기 위한 반복문
    for i in range(start, cards_num):
        deck[start], deck[i] = deck[i], deck[start]     # 순서 바꾸기
        permutation(start + 1, deck)                    # 다음 카드를 확인해보자
        deck[start], deck[i] = deck[i], deck[start]     # return 되었다면 바꾸기 이전으로 되돌리자


for test_case in range(1, int(input()) + 1):
    # 숫자 입력이 붙어서 들어왔기 때문에 숫자를 하나씩 꺼내서 int형으로 배열에 저장해준다.
    my_deck = ' '.join(input()).split()
    result = False
    for i in range(len(my_deck)):
        my_deck[i] = int(my_deck[i])

    deck_checker = []
    permutation(0, my_deck)         # 카드의 조합을 찾으면서 베이비진을 판별

    for is_true in deck_checker:    # deck_checker를 순회하면서
        if is_true:                 # True값이 존재한다면
            result = True           # 어쨌든 베이비 진이 존재하므로
            break                   # 순회 중단

    print(result)
