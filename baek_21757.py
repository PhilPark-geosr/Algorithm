import sys
sys.stdin = open('input_21757.txt', 'r')

N = int(input())
num_list = list(map(int, input().split()))
sys.setrecursionlimit(10**9)

def get_partial_sum(arr):
    n = len(arr)
    s = [0]*(n+1)
    # s[i] - s[i-1]
    for i in range(1, n+1):
        s[i] = s[i-1] + arr[i-1]
    return s

p_sum = get_partial_sum(num_list)
# print(p_sum)

total_sum = p_sum[-1]
if total_sum %4 != 0: # 4로 안나눠 떨어지면
    print(0)
else: #가능성이 있으면
    dp = [[-1]*4 for _ in range(N+1)]
    base_num = total_sum//4
    def dfs(idx, cnt):
        # print(f"dfs{idx, cnt}")
        if idx > N:
            return 0
        if cnt ==3: #다 잘 나누었으면
            return 1

        if dp[idx][cnt] !=-1:
            return dp[idx][cnt]

        dp[idx][cnt] = 0

        if p_sum[idx] == (cnt+1)*(base_num): #경계를 나눌 수 있으면
            dp[idx][cnt] += dfs(idx+1, cnt+1) #경계를 나눈다
            dp[idx][cnt] += dfs(idx+1, cnt) #경계를 나누지 않는다
        else: #경계 못나누면
            dp[idx][cnt] += dfs(idx+1, cnt)

        return dp[idx][cnt]



    print(dfs(1,0))



