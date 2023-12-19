import sys
sys.stdin = open('input_10942.txt','r')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input())
numlist = list(map(int, input().split()))
numlist.insert(0,0)
M = int(input())

dp = [[-1]*(N+1) for _ in range(N+1)]

def dfs(i, j):
    if i >=j:
        return True
    if dp[i][j] !=-1:
        return dp[i][j]
    
    dp[i][j] = False
    if numlist[i] == numlist[j]:
        check = dfs(i+1, j-1)
        if check == True:
            dp[i][j] = True
    
    return dp[i][j]




# main
for _ in range(M):
    s,e = map(int, input().split())
    if dfs(s,e) == True:
        print(1)
    else:
        print(0)
