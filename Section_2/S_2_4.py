import sys
sys.stdin=open("input.txt","rt")

### 내 풀이 ###

# 일단 생각한건 평균값에서 학생들의 값을 빼고
# 그 값의 절댓값이 가장 작은 값이 평균에 가장 가까운 값이다.
# 만약 값이 같다면 list에서 인덱스가 작은 값을 출력.

# N= int(input())
# P= list(map(int, input().split()))

# sum = 0
# Q=[]

# for i in P:
#     sum += i   
# average = sum/len(P)

# for i in P:
#     Q.append(abs(average-i))

# QMin=Q[0]

# for i in Q:
#     if i<QMin:
#         QMin=i
        
# print(P[Q.index(QMin)], Q.index(QMin))


### 강의 풀이 ###

n = int(input())
a = list(map(int, input().split()))
# 소수첫째자리에서 반올림하는 함수 round, list 전체 합은 sum(a)로 가능
ave=round(sum(a)/n)
min=2147000000
# 학생의 번호가 필요하기 때문에 index값을 반환해주는 enumerate필요.
for idx, x in enumerate(a):
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        # 거리 값이 같을 때는 큰값이 답이기 떄문에 
        res=idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1
        # 점수가 큰 학생으로 바꿔줌. (ex 평균이 74이고 73,75 일때)
        # 만약 뒤에 점수가 75점이 똑같이 나오면 번호는 바꿔주지 않음.

print(ave, res) 
        

    
    
        
