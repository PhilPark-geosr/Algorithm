import sys
sys.setrecursionlimit(10**9)
#sys.stdin = open('input_2281.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

# 여러 줄을 한 번에 읽기
num_list = [int(input()) for _ in range(N)]
num_list.insert(0, 0)
# print(num_list)
dp = [[float('inf')]*(M+1) for _ in range(N+1)]

#dp[i][count] : i번째 원소까지 배치하고 마지막줄이 lastline만큼 차지했을 때, 생기는 공백의 최솟값
global min_space
def dfs(i, lastline, result):
    global min_space
    # print(f"dfs{i, lastline, result}")

    if i==N:
        if result < min_space:
            min_space = result
        return
            
    if dp[i][lastline] <= result:
        # print(f"dp{i,lastline}은 이미 젤 작습니다 {dp[i][lastline], result}")
        return
    
    dp[i][lastline] = result
    if i+1 <=N:
        if lastline + 1 + num_list[i+1] <=M:
            dfs(i+1, lastline + 1 + num_list[i+1], result)
        dfs(i+1, num_list[i+1], result + (M-lastline)**2)
        
min_space = float('inf')
dfs(1, num_list[1],0)
print(min_space)