import sys
import itertools
sys.stdin = open('input_12689.txt', 'r')

N = int(input())
SCV = list(map(int, input().split()))
while len(SCV) < 3:
    SCV += [0]
# dp
attack = [-9,-3,-1]
attacklist = list(map(list, itertools.permutations(attack)))
# print(attacklist)

dp = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)]

def dfs(i,j,k):
    # print(f"dfs{i,j,k}")
    if dp[i][j][k] !=-1:
        return dp[i][j][k]
    if i==0 and j==0 and k==0:
        return 0
    dp[i][j][k] = float('inf')
    caselist = []
    for elem in attacklist:
        new_i, new_j, new_k = i+elem[0], j+elem[1], k +elem[2]
        if i + elem[0] <0: 
            new_i = 0
        if j + elem[1] <0:
            new_j = 0
        if k + elem[2] <0:
            new_k = 0
        caselist.append(dfs(new_i, new_j, new_k))
    dp[i][j][k] = min(caselist) +1

    
    return dp[i][j][k]
print(dfs(SCV[0], SCV[1], SCV[2]))


# else:
#     dp = [[-1 for _ in range(61)] for _ in range(61)]