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

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
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

# 실전 문제 4-2. 왕실의 나이트 ** 다시 풀어볼 문제
## 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
## 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
## 8*8 좌표 평면상에서 현재 나이트의 좌표가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 구하시오.
input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 #ord(문자) -> 유니코드 정수를 반환
steps = [(-2,-1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_col = column + step[1]
    if next_row < 1 or next_row > 8 or next_col < 1 or next_col > 8:
        continue
    result += 1
    """
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1
    """
print(result)

# 실전 문제 4-3. 게임 개발
"""
아직 나에게는 어려워서 pass. 다음에 풀어보자 ~
"""
