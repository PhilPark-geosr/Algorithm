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

dp = [[[float('inf') for _ in range(61)] for _ in range(61)] for _ in range(61)]

dp[SCV[0]][SCV[1]][SCV[2]] =0 #12, 10, 4를 만드는데 필요한 최소 공격횟수 는 0번

for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            if dp[i][j][k] ==float('inf'): #값없으면 통과
                continue
            for elem in attacklist:
                new_i, new_j, new_k = i+elem[0], j+elem[1], k +elem[2]
                if i + elem[0] <0: 
                    new_i = 0
                if j + elem[1] <0:
                    new_j = 0
                if k + elem[2] <0:
                    new_k = 0
                dp[new_i][new_j][new_k] = min(dp[new_i][new_j][new_k], dp[i][j][k]+1)

print(dp[0][0][0])
