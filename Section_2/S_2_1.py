
import sys
sys.stdin=open("input.txt","rt")

# 내 풀이
# N, K = map(int, input().split())
# q=[]

# for i in range(1, N+1):
#     if N%i==0:
#         q.append(i)

# if k-1 <= len(q):
#     print(q[K-1])
# else :
#     print(-1)

## range범위 설정을 잘못하였음! 
## for else 구문을 사용하면 굳이 리스트에 넣을 필요가 없음
## 어차피 1부터 숫자가 작은순서대로이기 때문에 ㄱ그냥 하면됨 

#강의 풀이
n, k = map(int, input().split())
cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)

# 정상적으로 끝나면 else 실행, k번째를 찾으면 break로 
