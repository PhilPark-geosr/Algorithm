import sys
import math
sys.setrecursionlimit(10**9)
sys.stdin = open('input_1344.txt','r')
pa = int(input())/100
pb = int(input())/100

# print(pa, pb)
def is_prime(x):
    if x ==0 or x ==1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i ==0: #나눠떨어지면 소수 아니다
            return False
    return True

dp = [[[-1 for _ in range(19)] for _ in range(19)] for _ in range(19)]

def dfs(time, a, b):

    if time ==0:

        if a ==0 and b ==0:
            return 1
        else:
            return 0

    if dp[time][a][b] !=-1:
        return dp[time][a][b]
    dp[time][a][b] =0
    if a-1 >=0 and b >=0:
        dp[time][a][b] += dfs(time-1, a-1, b)*pa*(1-pb)
    if a>=0 and b-1>=0:
        dp[time][a][b] += dfs(time-1, a, b-1)*(1-pa)*pb
    if a-1>=0 and b-1>=0:
        dp[time][a][b] += dfs(time-1, a-1, b-1)*pa*pb
    if a>=0 and b>=0:
        dp[time][a][b] += dfs(time-1, a, b)*(1-pa)*(1-pb)

    return dp[time][a][b]

answer = 0
for i in range(19):
    for j in range(19):

        if is_prime(i) == True or is_prime(j) == True:
            # print(i,j)
                # print(dp[18][i][j])
            answer += dfs(18,i,j)
print(answer)