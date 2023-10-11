### 최솟값 구하기 ###
arr=[5, 3, 7, 9, 2, 5, 2, 6]
#파이썬에서 가장 큰 값이 들어간다고 생각(무한대로 초기화)
#arrMin=float('inf')
arrMin=arr[0] 
# 0번째 값으로 비교해줄 수 도 있다.

for i in range(len(arr)):
    if arr[i]< arrMin:
        arrMin=arr[i]
print(arrMin)

