import sys
sys.stdin = open('input_12969.txt', 'r')
dp = [[[[False]*436 for k in range(31)] for j in range(31)] for i in range(31)]
N, K = map(int,input().split())

global answer
answer = ""
def dfs(a, b, c, cnt, result):
    print(f"dfs{a,b,c, cnt}")
    global answer
    if a+ b+c == N:
        if cnt == K:
            answer = result
        return
    if dp[a][b][c][cnt] == True:
        return
    dp[a][b][c][cnt] = True #방문표시
    dfs(a+1, b, c, cnt, result+ "A")
    dfs(a, b+1, c, cnt+a, result+ "B")
    dfs(a, b, c+1, cnt+a+b, result+ "C")
    
dfs(0,0,0,0, "")
if answer == "":
    print(-1)
else:
    print(answer)


