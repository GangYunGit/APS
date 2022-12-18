# 2001를 풀며

- 2차원 배열을 입력받을 때 자주 써먹는 코드
  
  ```python 
  for row in range(N):
      fly = list(map(int, input().split()))
      fly_cell.append(fly)
  ``` 
  - 행 하나의 순회마다 하나의 리스트가 필요하기 때문에, map(input().split())으로 N개의 정수를 입력받고 이를 리스트에 저장하면 총 N * N의 행렬을 입력받을 수 있다!
  
---

- (*)처음에 반복문 틀을 잡을 때 접근 자체는 옳게 한 것 같다. 하지만 파리채 범위(M * M)를 잡아주는 내부 for문에서 M * M 칸의 합을 저장하기 위해, 처음에는 List에 저장하여 sum함수를 이용하려 했지만 변수가 너무 복잡해져서 깔끔하게 쓸 수 있는 방법을 생각해보았다. 고민 끝에 어짜피 이차원 배열의 원소 한 개는 정수니까 (i,j) 중첩 반복문을 돌며 M * M개의 합을 += 연산자로 받도록 했다.
  
  ```python
  for row in range(N - M + 1):  # ***
      for column in range(N - M + 1): # ***
          M_rooms = 0 # *
          for i in range(M):  # *
              for j in range(M):  # *
                  M_rooms += fly_cell[row + i][column + j]  # *
          M_rooms_list.append(M_rooms)  # *
  ```

---

- (***)반복문에서 range를 이용한 iter범위 설정시, 예시를 이용하여 숫자를 대입해 보고, 숫자를 키워가며 일반화 시켜보면 주어진 변수들을 어떻게 활용할 수 있을지 감을 잡을 수 있다.
