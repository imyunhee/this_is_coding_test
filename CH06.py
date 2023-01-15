# 선택 정렬 예시
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)): #i=0부터
    min_index = i
    for j in range(i+1, len(array)): #j=1부터
        if array[min_index] > array[j]:
            min_index = j #가장 작은 원소의 index를 min_index에 저장
    array[i], array[min_index] = array[min_index], array[i] #swap

print(array)

# 삽입 정렬 예시

