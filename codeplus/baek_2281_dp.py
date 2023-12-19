import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input_2281.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = []
for _ in range(N):
    elem = int(input())
    num_list.append(elem)
num_list.insert(0,0)
# print(num_list)
dp = [[-1]*(M+1) for _ in range(N+1)]
#dp[i][count] : i번째 원소까지 배치하고 마지막줄이 count만큼 차지할때, i+1~ N번째까지 발생하는 공백의 최솟값
def dfs(i, count):
    # print(f"dfs{i,count}")
    if i == N:
        return 0
    if dp[i][count] !=-1:
        return dp[i][count]
    if count + num_list[i+1] +1 <=M:
        dp[i][count] = min(dfs(i+1, count + num_list[i+1] +1), dfs(i+1, num_list[i+1]) + (M-count)**2)
    else:
        dp[i][count] = dfs(i+1, num_list[i+1]) + (M-count)**2
    
    return dp[i][count]


print(dfs(1,num_list[1]))






