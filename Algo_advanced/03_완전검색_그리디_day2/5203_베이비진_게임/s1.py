import sys
sys.stdin = open('input.txt', encoding='utf-8')


# 카드의 순열을 구해주는 함수
def permutation(arr, end, start):
    if len(pick) == end:                    # 뽑고 싶은 개수 만큼 뽑았다면 return
        player_comb.append(list(pick))      # return 하기 전에 만들어진 순열을 배열에 저장
        return

    for i in range(len(arr)):
        if used[i] == 0:
            used[i] = 1
            pick.append(arr[i])
            permutation(arr, end, start + 1)
            used[i] = 0
            pick.pop()


# baby-gin을 판별해주는 함수
def is_baby_gin(deck):
    # 카드의 개수가 3개 이상일 때부터 3장씩 검사
    for i in range(len(deck) - 2):
        if deck[i] + 2 == deck[i + 1] + 1 == deck[i + 2]:   # run
            return True

        if deck[i] == deck[i + 1] == deck[i + 2]:           # triplet
            return True

    return False


# 어떤 플레이어가 이겼는지 판별해주는 함수
def is_player_won(player):
    permutation(player, 3, 0)       # 가능한 카드의 순열을 구해서

    for deck in player_comb:        # 순열을 모두 확인하며
        if is_baby_gin(deck):       # 베이비 진이 있는지 체크하고
            return True             # run 혹은 triplet 을 만나는 순간 리턴


for test_case in range(1, int(input()) + 1):
    card_draw = list(map(int, input().split()))

    player_1 = [card_draw[2 * i] for i in range(2)]         # 우선 player_1의 카드 2장을 미리 뽑아놓고
    player_2 = [card_draw[2 * i + 1] for i in range(2)]     # 우선 player_2의 카드 2장을 미리 뽑아놓고
    result = 0

    for i in range(2, 6):

        player_1.append(card_draw[2 * i])          # 여기에서 한장 씩 더 받아서 3장부터 시작한다
        player_2.append(card_draw[2 * i + 1])      # 여기에서 한장 씩 더 받아서 3장부터 시작한다

        used = [0] * len(player_1)                 # 순열을 구하기 위한 used 리스트
        pick = []                                  # 한 싸이클 당 뽑은 순열을 저장할 변수
        player_comb = []                           # 싸이클을 돌면서 뽑힌 순열들을 저장할 변수

        if is_player_won(player_1):         # player_1이 이겼다면
            result = 1                      # 1을 저장하고
            break                           # 반복문 탈출

        if is_player_won(player_2):         # player_2이 이겼다면
            result = 2                      # 2을 저장하고
            break                           # 반복문 탈출

    print(f'#{test_case} {result}')
