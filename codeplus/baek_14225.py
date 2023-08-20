import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input_14225.txt', 'r')

N = int(input())
number_list = list(map(int, input().split()))

dp = [-1]*(20*100000+1)

def dfs(i, value):
    # print(f"dfs{i, value}")
    dp[value] = True
    if i >=N-1:
        return
    
    dfs(i+1, value+ number_list[i+1])
    dfs(i+1, value)
    
# print(dp)
dfs(0, number_list[0])
dfs(0, 0)


# main
answer = float('inf')
for i in range(1, len(dp)):
    if dp[i] ==-1:
        answer = i
        break

print(answer)




