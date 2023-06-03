import sys
import heapq

sys.stdin = open("input_4485.txt", "r")
dx = [1,-1,0, 0]
dy = [0,0, 1,-1]
# define functionality
def dijikstra(array):
    q = []
    n = len(array)
    distance = [[float('inf')]*n for _ in range(n)]
    distance[0][0] = array[0][0] # (0,0) ~ (0,0)은 최단거리 0
    heapq.heappush(q, (array[0][0], 0, 0 ))
    while q:
        dist, now_i, now_j = heapq.heappop(q)
        if distance[now_i][now_j] < dist: # 이미 처리되었으면
            continue
        for k in range(4):
            new_i, new_j = now_i + dx[k], now_j + dy[k]
            # print(new_i, new_j)
            if 0<=new_i<n and 0<=new_j<n:
                new_cost = dist + graph[new_i][new_j]
                if new_cost < distance[new_i][new_j]:
                    distance[new_i][new_j] = new_cost
                    heapq.heappush(q, (new_cost, new_i, new_j))
    return distance[n-1][n-1]
                    
flag =True
num_of_problem = 1
while flag == True:
    n = int(input())
    # print(n)
    if n == 0:
        flag = False
    else:
        # make a grpah
        graph = []
        for _ in range(n): #O(n^2)
            line = list(map(int, input().split()))
            graph.append(line)
        
        result = dijikstra(graph) 
        print(f"Problem {num_of_problem}: {result}")
        num_of_problem +=1

        