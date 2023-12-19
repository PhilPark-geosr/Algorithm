import sys
sys.stdin = open('input_2011.txt', 'r')
sys.setrecursionlimit(10**8)

S = input()
N = len(S)

dp = [-1]*(N+1)

def dfs(i):
    if i == 0:
        return 1
    if i ==1:
        if int(S[i-1:i]) !=0:
            return 1
        else:
            return 0
    if dp[i] != -1:
        return dp[i]

    if int(S[i-1:i]) == 0 and (10<= int(S[i-2:i]) <= 26):
        dp[i] = dfs(i-2)
    elif int(S[i-1:i]) != 0  and (10<= int(S[i-2:i]) <= 26):
        dp[i] = dfs(i-1) + dfs(i-2)
    elif int(S[i-1:i]) == 0 and ~(10<= int(S[i-2:i]) <= 26):
        dp[i] = 0
    else:
        dp[i] = dfs(i-1)
    dp[i] %= 10**6

    return dp[i]





# ------------------- main ---------------------- #
#
answer = dfs(N)

if answer == -1:
    print(0)
else:
    print(answer)