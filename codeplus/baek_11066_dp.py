import sys
sys.stdin = open('input_11066.txt', 'r')
sys.setrecursionlimit(10**8)
#input = sys.stdin.readline
# dfs함수정의
def dfs(i, j): 
    # print(f"dfs{i,j}")
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = min([dfs(i,k) + dfs(k+1, j) for k in range(i, j)]) + file_sum[j]- file_sum[i-1]
    return dp[i][j]

T = int(input()) # test case

for _ in range(T):
    N = int(input()) #합칠 파일의 갯수
    filelist = list(map(int, input().split()))

    # 누적합 구해놓기
    file_sum = [0]*(N+1)
    # file_sum[1] = filelist[0]
    for i in range(N):
        file_sum[i+1] = file_sum[i] + filelist[i]
    # print("누적합", file_sum)

    # dp initialize
    dp = [[-1]*(N+1) for _ in range(N+1)]
    # 결과
    answer = dfs(1, N) #다합치는데 드는 최소비용
    print(answer)




