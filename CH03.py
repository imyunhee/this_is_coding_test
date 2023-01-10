#예제 3-1. 거스름돈

##N원을 거슬러 줄 때 동전의 최소 개수를 구하라. (단, N은 10의 배수이다.)

N = input("N을 입력하시오. : ")
n = int(N)
count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n//coin
    n %= coin

print(N, "원을 거슬러 줄 때, 동전의 최소 개수는", count, "개 이다.")

####시간복잡도 = O(K)이다, 동전의 총 종류에만 영향을 받고, 거슬러 줘야 하는 금액의 크기와는 무관하다.


#실전 3-2. 큰 수의 법칙

##배열의 크기 N, 숫자가 더해지는 횟수 M, 연속할 수 있는 횟수 K 일 때 더하여 구할 수 있는 가장 큰 수를 구하여라.

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

first = data[0]
second = data[1]

x = M // (K+1)
y = M % (K+1)

result = (first * (x*K + y)) + (second * x)
print(result)

#실전 3-3. 숫자 카드 게임

##N*M 카드에서 같은 행의 카드 중 가장 작은 수의 카드를 뽑을 때 가장 큰 숫자의 카드를 뽑으시오.

N, M = map(int, input().split())

result = 0
for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(min_value, result)

print(result)

#실전 3-4. 1이 될 때까지

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