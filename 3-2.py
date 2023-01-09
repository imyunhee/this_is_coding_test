#예제 3-2. 큰 수의 법칙

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
print(x, y, first, second)