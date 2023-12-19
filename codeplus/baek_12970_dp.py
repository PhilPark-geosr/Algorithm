import sys
sys.stdin = open('input_12970.txt', 'r')
N, K = map(int, input().split())

dp = [[[False]*(K+1) for _ in range(K+1)] for _ in range(N+1)]

global answer
def dfs(i, cnt, a_count, result):
    global answer
    # print(f"dfs{i,cnt, result}")
    if i > N or cnt > K or a_count > K:
        return
    
    if i== N and cnt ==K:
        answer = result
        return

    if dp[i][cnt][a_count] == True:
        # print('이미 존재합니다')
        return

    dp[i][cnt][a_count] = True
    
    dfs(i+1, cnt + a_count, a_count, result+"B")
    dfs(i+1, cnt , a_count+1, result+"A")



# answer
answer = -1
dfs(0, 0, 0, "")
print(answer)