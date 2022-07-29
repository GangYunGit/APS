# 1974를 풀며

- 전형적인 2차원 배열 문제같다. 이제 2차원 배열을 입력으로 받는건 익숙해진 듯 하다. 하지만 여전히 반복문 내부에서 `특정 시점이나 루프를 되돌아 갈 때 초기화가 되어야 할` 변수의 위치를 잘 잡지는 못한다. 그래도 틀렸을 때 어느부분에서 틀리는지 찾아내는 속도가 빨라진 듯 하다
  
---

## 핵심 코드

- 우선 가로 방향과 세로방향을 먼저 검증한다. 처음에는 가로와 세로를 각각 따로 탐색하려고 했으나, 그냥 행 우선 순회를 열 우선 순회로 바꾸기만 하면 되는거구나 하는 생각이 나서 한번에 검증하였다. 가로 세로의 경우 모두 and로 한번에 묶어서 둘다 맞으면 confirm변수는 그대로 0을 유지한다.
  
  ```python
  for i in puzzle_length:
        is_row = 0
        is_column = 0
        for j in puzzle_length:
            is_row += puzzle[i][j]
            is_column += puzzle[j][i]
        if is_row == 45 and is_column == 45:
            continue
        else:
            confirmed += 1
  ```

---

- 그 다음 3x3칸 9개를 검증한다. 우선 (0,0) ~ (2,2) 인덱스를 점검하고 가로세로의 인덱스 사이에 0, 3, 6을 차례로 끼워넣어 더하면 3칸짜리 정사각형이 9개를 만들 수 있을 것이라 생각했고, 수행 결과도 일치했다. 이후에는 똑같이 confirm변수에 검증한 정보를 저장한다.

  ```python
  for k_i in range(0, 9, 3):
        for k_j in range(0, 9, 3):
            is_9 = 0
            for i in range(3):
                for j in range(3):
                    is_9 += puzzle[i + k_i][j + k_j]
            if is_9 == 45:
                continue
            else:
                confirmed += 1
  ```
- (***)dasd
