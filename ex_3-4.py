#예제 3-4. 1이 될 때까지

## 1. N에서 1을 뺀다.
## 2. N을 K로 나눈다.
## 1번 또는 2번으로 N을 1로 만드는 최소 횟수를 구하여라.

N, K = map(int, input().split())

count = 0
while N >= K:
    while N%K !=0:
        N -= 1
        count += 1
    N //= K
    count += 1

count += (N-1)

print(count)