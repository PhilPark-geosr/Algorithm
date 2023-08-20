import sys
sys.stdin = open('input_10942.txt', 'r')
# input = sys.stdin.readline

N = int(input())
numlist = list(map(int, input().split()))
numlist.insert(0,0)

M = int(input())
q_list = []
for _ in range(M):
    a,b = map(int, input().split())
    q_list.append((a,b))

def ispal(s,e, num):
    if s > e:
        return False
    
    if dp[s][e] !=-1: #값이 있으면 바로 리턴
        return dp[s][e]
    
    if s ==e:
        dp[s][e] = True
        return True

    if num[s] != num[e]:
        dp[s][e] =False #기록
        return False
    else:
        if s-e ==1:
            dp[s][e] = True
        else:
            check= ispal(s+1, e-1, num)
            if check == True:
                dp[s][e] = True
            else:
                dp[s][e] = False

    return dp[s][e]

dp = [[-1]*(N+1) for _ in range(N+1)]
for s,e, in q_list:
    if ispal(s, e, numlist) == True:
        print(1)
    else:
        print(0)