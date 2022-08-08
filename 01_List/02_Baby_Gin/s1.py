T = int(input())

for test_case in range(1, T + 1):
    my_deck = list(map(int, input()))
    result = 0  # Baby-gin인지 판별하기 위한 변수
    loop_count = 0  # While문의 1oop횟수를 제한하기 위한 변수

    # 가능한 카드의 숫자 0~9를 index로 쓰기 위한 배열 생성
    # 숫자 9가 첫 번째로 오는 'run'을 검사할 때 index error가 나는 것을 방지 하기 위해 2칸을 추가
    card_slot = [0] * 12

    for i in range(6):  # 내가 가진 카드의 각 숫자가 몇 장씩 있는지를 card_slot이라는 배열에 저장
        card_slot[my_deck[i]] += 1

    while True:
        for j in range(len(card_slot)):  # triplet을 검사하는 반복문
            # 특정 index의 value가 3 또는 6이라면 값을 3 감소 후 result에 +1
            if card_slot[j] > 0 and card_slot[j] % 3 == 0:
                card_slot[j] -= 3
                result += 1

        for k in range(len(card_slot)):  # run을 검사하는 반복문
            # 연속된 3개의 숫자가 있다면 각 index의 value를 1씩 감소 후 result에 +1
            if card_slot[k] > 0 and card_slot[k + 1] > 0 and card_slot[k + 2] > 0:
                card_slot[k] -= 1
                card_slot[k + 1] -= 1
                card_slot[k + 2] -= 1
                result += 1

        loop_count += 1
        if loop_count == 2:  # loop가 2번 반복되며 총 4번의 triplet, run 검사가 이루어짐
            break

    if result == 2:  # triplet, 혹은 run을 합친 값이 2이면 Baby gin
        print(1)
    else:
        print(0)
