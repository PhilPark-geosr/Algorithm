import sys
sys.stdin = open('input_11660.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0]*(N+1)]
for _ in range(N):
    line = list(map(int, input().split()))
    line.insert(0,0)
    graph.append(line)
# print('graph', graph)

s = [[0]*(N+1) for _ in range(N+1)]
# 2차원 누적합 구하기
for i in range(1, N+1):
    for j in range(1, N+1):
        s[i][j] = s[i-1][j] + s[i][j-1] -s[i-1][j-1] + graph[i][j]

# print(s)
def get_sum(a,b,c,d):
    return s[c][d] - (s[a-1][d] + s[c][b-1]) + s[a-1][b-1]

# 정답
for _ in range(M):
    a,b,c,d = map(int, input().split())
    # print('a,b,c,d', a,b,c,d)
    print(get_sum(a,b,c,d))



