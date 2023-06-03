import sys

sys.stdin = open("input_14916.txt", 'r')

n = int(input())

# sol1 dp풀이 
# coinlist = [5,2]
# #initialize dp
# #dp[i] : i월을 거슬러 주는 동전의 최소
# dp = [float('inf')]*(n+1)
# dp[0] =0

# for coin in coinlist: #5원과 2원으로 거슬러줄수 있는 동전의 최소 
#     for i in range(coin, n+1):
#         dp[i] = min(dp[i], 1+ dp[i-coin])

# print(dp[n])

# sol2 greedy

# 최대한 많은 개수 구한다!
num_5, res = divmod(n, 5)

cnt =0
while num_5 >=0:
    if res %2 !=0: # 2로 나누어떨어지지 않을경우
        num_5-=1
        res += 5
    else: # res % 2==0:
        cnt = res//2
        break

if num_5 <0:
    print(-1)
else:
    print(num_5 + cnt)

