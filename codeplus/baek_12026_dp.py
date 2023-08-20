import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("input_12026.txt", 'r')

N = int(input())
block = input()
block = "#" + block
# print("block", block)

# dp 
# dp[i] : i번째에 도달할수 있는 최소 에너지
dp = [-1]*(N+1)

def dfs(i):
    # print(f"dfs{i}, {block[i]}")
    if i==1:
        return 0
    if dp[i] !=-1:
        return dp[i]
    
    if block[i] == "B":
        caselist = [dfs(k) + (k-i)**2 for k in range(1, i) if block[k]=="J"]
        if caselist :
            dp[i] = min(caselist)
        else:
            dp[i] = float('inf')

    elif block[i] == "O":
        caselist = [dfs(k) + (k-i)**2 for k in range(1, i) if block[k]=="B"]
        if caselist :
            dp[i] = min(caselist)
        else:
            dp[i] = float('inf')
    else: #block[i] == "J"
        caselist = [dfs(k) + (k-i)**2 for k in range(1, i) if block[k]=="O"]
        if caselist :
            dp[i] = min(caselist)
        else:
            dp[i] = float('inf')
    return dp[i]





# answer
if dfs(N) == float('inf'):
    print(-1)
else:
    print(dfs(N))
