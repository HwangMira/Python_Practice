import sys
sys.stdin=open("input.txt","rt")

# T = int(input())
# q=[]
# p=[]

# for i in range(T):
#     N, s, e, k = map(int, input().split())
#  굳이 for문 또 써서 N번째까지로 리스트를 만들 필요 없이
#  한번에 리스트로 넣으면서 입력받으면됨!
#     for j in range(N):
#         q=list(map(int, input().split()))
#         for z in range(s+1, e+1):
#             p.append(z)
#     p.sort()
#     print("#",i,' ',p[k+1])

T= int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a=list(map(int, input().split()))
    # 바로 추출 a리스트로 추출할 수 있다. 
    # 새로 리스트를 만들필요 없음. 
    a=a[s-1:e]
    a.sort() 
    print("#%d %d" %(t+1, a[k-1]))
    