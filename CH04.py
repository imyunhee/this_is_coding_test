# 예제 4-1. 상하좌우

## 시뮬레이션 유형: 개체를 차례대로 이동시킴
X = 1
Y = 1
N = int(input())
plans = input().split()

for moving in plans:
    if moving == 'L':
        if Y == 1:
            continue # continue: 해당 반복 벗어남.
        Y -= 1
    elif moving == 'R':
        if Y == N:
            continue
        Y += 1
    elif moving == 'U':
        if X == 1:
            continue
        X -= 1
    else:
        if X == N:
            continue
        X += 1


print(X, Y)

### 시간복잡도 = O(N), N = 이동 횟수


# 예제 4-2. 시각
## 00시 00분 00초 ~ N시 59분 59초까지의 모든 시각 중에 3이 포함된 경우의 수
N = int(input())

if N < 3:
    result = (N+1)*6*10*6*10 - (N+1)*5*9*5*9
else:
    result = (N+1)*6*10*6*10 - N*5*9*5*9

print(result)
## 완전 탐색 알고리즘: 가능한 경우의 수를 모두 검사해보는 탐색 방법
h = int(input())

count=0
for i in range (h+1): #시
    for j in range(60): #분
        for k in range(60): #초
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)