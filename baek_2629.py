import sys
sys.stdin = open("input_2629.txt", "r")

n = int(input()) # 구슬개수
ball_list = list(map(int, input().split()))
m = int(input()) # 확인하고 싶은 무게 갯수
weight_list = list(map(int, input().split()))

dp = [[0]*40001 for _ in range(n)]
#dp[i][weight] 0~i번째 구슬로 만들수 있는 무게중 weight를 만들수 있는지 여부


def dfs(v, w):
    # print(f"dfs{v,w, result}")
    if v == n:
        return
        
    new_list = [w + ball_list[v], abs(w - ball_list[v]), w]
    # print(new_list)
    for new_w in new_list:
        if dp[v][new_w] == 0:
         
            dp[v][new_w] =1
            dfs(v+1, new_w)
            
dfs(0, 0)


for elem in weight_list:
    # print(elem, end =" ")
    if dp[n-1][elem] ==1:
        print('Y', end =" ")
    else:
        print('N',end =" ")
