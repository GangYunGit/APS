# 거리두기_확인하기

def solution(places):
    print(places)
    answer = []

    # 델타 검색
    # 상 상2 우상 우 우2 우하 하 하2 좌하 좌 좌2 좌상
    dx = [0, 0, 1, 1, 2, 1, 0, 0, -1, -1, -2, -1]
    dy = [-1, -2, -1, 0, 0, 1, 1, 2, 1, 0, 0, -1]
    for place in places:
        catch = []

        for x in range(5):
            for y in range(5):
                if place[x][y] == "P":
                    for i in range(12):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if place[nx][ny] == "P":

                                if abs(nx - x) + abs(ny - y) < 2:
                                    catch.append(1)
                                    break
                                else:
                                    if i == 2 and (place[x + 1][y] == "O" or place[x][y - 1] == "O"):
                                        catch.append(1)
                                    if i == 5 and (place[x + 1][y] == "O" or place[x][y + 1] == "O"):
                                        catch.append(1)
                                    if i == 8 and (place[x - 1][y] == "O" or place[x][y + 1] == "O"):
                                        catch.append(1)
                                    if i == 11 and (place[x - 1][y] == "O" or place[x][y - 1] == "O"):
                                        catch.append(1)
                                    if i == 1 and place[x][y - 1] == "O":
                                        catch.append(1)
                                    if i == 4 and place[x + 1][y] == "O":
                                        catch.append(1)
                                    if i == 7 and place[x][y + 1] == "O":
                                        catch.append(1)
                                    if i == 10 and place[x - 1][y] == "O":
                                        catch.append(1)

        if 1 in catch:
            answer.append(0)
        else:
            answer.append(1)
    print(answer)
    return answer


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
