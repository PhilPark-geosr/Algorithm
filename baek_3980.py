import sys
import collections
sys.stdin = open('input_3980.txt', 'r')
sys.setrecursionlimit(10**9)

T = int(input()) #테스트 케이 스 수
for _ in range(T):
    point = [[0]*12]
    for _ in range(11):
        line = [0] + list(map(int, input().split()))
        point.append(line)
    # print('point', point)
    graph = collections.defaultdict(list)
    for i in range(1, 12):
        for j in range(1, 12):
            if point[i][j] !=0:
                graph[i].append(j)
    # print('graph', graph)
    position = [0]*(12)
    global max_score
    max_score = 0
    def dfs(v, pos, score):
        global max_score
        # print(f"dfs{v, pos, score}")
        if v ==11:
            # print('score', score)
            if score > max_score:
                max_score = score
            return

        position[pos] = 1
        caselist = graph[v+1]

        for new_pos in caselist:
            if position[new_pos] == 0:
                dfs(v+1, new_pos, score + point[v+1][new_pos])
        position[pos] = 0
    dfs(0, 0, 0 )
    print(max_score)