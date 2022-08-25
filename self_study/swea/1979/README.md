# 1979를 풀며

- map()함수에 대해 배우기 이전이라 map사용에 미숙했었다.
  
  ```python
  N_K = list(map(int, input().split()))   # 수정 전
  
  N, K = map(int, input().split())        # 수정 후
  ```
  
  - split메소드를 사용하여 input()함수에 각각 대입시키는 것이므로 굳이 list로 나눠서 넣을 필요 없이 콤마(,)로 구분하면 된다

- 조건을 `하나로만 묶어서 생각하지말고`, 한번에 해결이 안되면 `조건을 중첩시켜 해결`하려고 노력해보자

- 변수를 설정할 때 `반복문 내부에서 초기화되는 시점`을 잘 생각하여 설정하자

--- 

## 핵심 코드

```python
for row in range(N):
    count = 0
    for column in range(N):
        if puzzle[row][column] == '1':
            count += 1
        else:
            if count == K:
                is_K += 1
            count = 0
    if count == K:
        is_K += 1
```

- 문제 풀이 과정
  
  1. 예를들어 K = 3일 때, 처음에는 한 행을 기준으로 문자열을 만들고 '01110', '11101'과 같이 들어오는 것을 판별하려고 했지만 이를 조건문으로 표현하기가 힘들어 다른 방법을 생각해 보았다.
  
  2. 1이 몇 개 들어오는지를 count변수에 저장하고, is_K라는 변수를 연속해서 3번 들어왔을 때를 판별하는 변수로 사용하는 아이디어를 생각해 냈다.
  
  3. is_K를 이용하여 판별하는 코드를 반복문 내에 어떻게 배치시킬지를 많이 고민했다. else문에서 `count = 0`코드 때문에 '11101'과 같은 경우는 3이아니라 1로 카운트 되는 경우가 있어서 이 경우를 따로 생각해 주어야 했다.
  
  4. is_K가 연속된 1을 K개 만큼 찾은 직후 바로 다음 경우의 수는 1이 오거나, 0이 오거나, 반복이 끝나는 경우 3가지 이므로 코드를 다음과 같이 짰다.
     
     - '1'이 왔을 때에는 굳이 코드를 추가할 필요가 없었다. `count에서 이미 초과되기 때문`에 이미 작성된 조건문에서 걸러진다.
     - '0'이 왔을 때에는 `is_K 변수를 1 증가`
     - 반복이 끝났을 때에도 `is_K 변수를 1 증가`
     
     
  
  5. 행 우선 순회 코드를 열 우선 순회로 바꾸어 복붙한다.

