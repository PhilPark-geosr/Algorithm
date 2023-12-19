import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input_2668.txt', 'r')
import collections
input = sys.stdin.readline
N = int(input())

# numlist = [0]
# graph 생성 
graph = collections.defaultdict(list)
for i in range(1, N+1):
    elem= int(input())
    graph[elem].append(i)


# print("graph", graph)





global cycle_legth

answer = []
def dfs(v, length, cycle_list):
    global cycle_legth
    # print(f"dfs{v, length, cycle_list}")
    if visited[v] ==1: #사이클도달
        cycle_legth += length
        # print(cycle_list)
        answer.extend(cycle_list)
        # 방문한곳 체크
        for elem in cycle_list:
            ch[elem] =1
        return

    cycle_list = cycle_list + [v]
    visited[v] =1
    for new_v in graph[v]:
        dfs(new_v, length+1, cycle_list)
    cycle_list = cycle_list[:-1]

cycle_legth = 0
ch = [0]*(N+1)
for i in range(1, N+1):
    # print("ch", ch)
    
    if ch[i] ==0:
        visited = [0]*(N+1)
        dfs(i, 0, [])
    
print(cycle_legth)
answer.sort()
for elem in answer:
    print(elem)
# print(answer)

# a = [1,3,4]
# print(a[:-1])