import sys
sys.stdin = open('input_1495.txt', 'r')

N, S, M = map(int, input().split())
V = list(map(int, input().split()))
V.insert(0,0)

#dp[i][vol] # i번째 곡을 vol으로 연주할 수 있으면 1 , 없으면 -1
dp = [[-1]*(M+1) for _ in range(N+1)]

global answer

def dfs(i, vol): #값이 있으면 리턴
    global answer
    # print(f"dfs{i,vol}")
    if i == N:
        if vol > answer:
            answer = vol
        return
    if dp[i][vol] != -1:
        return 
    dp[i][vol] =1
    
    if vol + V[i+1] <=M: 
        dfs(i+1, vol + V[i+1])
    if vol - V[i+1] >=0: 
        dfs(i+1, vol - V[i+1])

answer =-1
dfs(0, S)
print(answer)