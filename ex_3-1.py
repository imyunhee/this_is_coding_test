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
