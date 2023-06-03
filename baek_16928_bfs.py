import sys
import collections
sys.stdin = open('input_16928.txt', 'r')

N, M = map(int, input().split())

# trans_dic 생성
trans_dic = dict()
for _ in range(N+M):
    a, b = map(int, input().split())
    trans_dic[a] = b #어디로 이동할지 지정

dp = [0]*101 # dp[i] : i번째 게임판에 도달하는데 필요한 최소 주사위 횟수

# def bfs():
#     q = collections.deque()
#     visited = [0]*101
#     q.append((1, 0)) 
#     visited[1] = 1 #방문처리
#     while q:
#         now, count = q.popleft() # 현재지점, 던진 주사위 수
#         # print(now, count)
#         # 이미 100번재 도달했으면 탈출
#         if dp[100] !=0: 
#             return dp[100]

#         for i in range(1,7):
#             new_des = now + i #새로 방문할 곳

#             # 전처리
#             if new_des in trans_dic: # 움직이는 곳에 있으면
#                 new_des = trans_dic[new_des]
            
#             # 실제움직여질 곳
#             if new_des <= 100 and visited[new_des] == 0 and dp[new_des] ==0 : #안가봤던 곳만 탐색 bfs 수행
#                 visited[new_des] =1
#                 dp[new_des] = count +1
                
#                 q.append((new_des, count+1))
                
#     return dp[100]
# refactoring   
def bfs():
    q = collections.deque()
    visited = [0]*101
    q.append(1) 
    visited[1] = 1 #방문처리
    while q:
        now = q.popleft() # 현재지점, 던진 주사위 수
        # print(now, count)
        # 이미 100번재 도달했으면 탈출
        if dp[100] !=0: 
            return dp[100]

        for i in range(1,7):
            new_des = now + i #새로 방문할 곳

            # 전처리
            if new_des in trans_dic: # 움직이는 곳에 있으면
                new_des = trans_dic[new_des]
            
            # 실제움직여질 곳
            if new_des <= 100 and visited[new_des] == 0 and dp[new_des] ==0 : #안가봤던 곳만 탐색 bfs 수행
                visited[new_des] =1
                dp[new_des] = dp[now] + 1
                q.append(new_des)
                
    return dp[100]
answer = bfs()
print(answer)