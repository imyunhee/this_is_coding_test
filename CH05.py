# 스택 stack
## 선입후출 또는 후입선출
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

# 큐 queue
## 선입선출 구조 first in first out
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 처음 들어온 원소부터 출력
queue.reverse()
print(queue) # 나중에 들어온 원소부터 출력

# 재귀 함수
## 재귀 함수 종료 예제
def recurive_function(i):
    if i == 10:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recurive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

recurive_function(1)

## 팩토리얼 예제
