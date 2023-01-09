#예제 3-3. 숫자 카드 게임

##N*M 카드 중 같은 행의 카드 중 가장 작은 수의 카드를 뽑을 때 가장 큰 숫자의 카드를 뽑으시오.

N, M = map(int, input().split())

result = 0
for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(min_value, result)

print(result)
