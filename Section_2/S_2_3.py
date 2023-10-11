import sys
sys.stdin=open("input.txt","rt")

# N, K = map(int, input().split())

# p = list(map(int, input().split()))

# sum = 0
# a=[]

# p.sort()
# for i in range(N):
#     for j in range(i+1, N):
#         for z in range(i+2, N):
#             sum=i+j+z
#             a.append(sum)
# 내풀이 : 3중 for문을 이용해서 더해서 리스트에 넣는 건 이해했는데
# 중복을 제거하는 자료구조는 몰라서 풀지 못했다.
            
# 강의 풀이
n, k = map(int, input().split())
a=list(map(int, input().split()))

#중복을 없애는 자료구조 !!*****
res=set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(i+2, n):
            res.add(a[i]+a[j]+a[m])
res=list(res)
res.sort(reverse=True)
print(res[k-1])

### 이 문제에서 외워야 할 것 ###
#sort 내림차순 정렬 reverse=True(T는 대문자로 작성)
# 이 문제에서 가져가야할 것 res=set() 중복을 없애는 자료구조 외우기. 
# res는 리스트화시켜줘야함. 리스트 자체가 아님 
