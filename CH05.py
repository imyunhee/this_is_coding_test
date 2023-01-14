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
### 반복적으로 구현
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print('반복적으로 구현:', factorial_iterative(5))
### 재귀적으로 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print('재귀적으로 구현:', factorial_recursive(5))

# DFS 예제
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [           #인접 리스트 방식(연결된 정보만 저장)
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

dfs(graph, 1, visited)

# BFS 예제
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [           #인접 리스트 방식(연결된 정보만 저장)
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
bfs(graph, 1, visited)

#실전 문제 5-3. 음료수 얼려 먹기
## 얼음 틀의 형태가 주어졌을 때, 총 만들 수 있는 아이스크림의 개수를 구하여라.


