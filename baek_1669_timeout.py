import sys
import collections
sys.stdin =open('input_1669.txt', 'r')
sys.setrecursionlimit(10**9)
global target

start, target = map(int, input().split())
global answer
answer = float('inf')
visited = collections.defaultdict(int)
def dfs(num, prev, depth):
    global target
    global answer
    # print(f"dfs{num, prev, depth, target}")
    if num >=target:
        return
    if num == target-1:
        answer = min(answer, depth)
        return

    visited[num] = 1
    if depth ==0:
        dfs(num+1, 1, depth+1)
    else:
        for new in [prev-1, prev, prev+1]:
            if new >=0 and visited[num + new] ==0:
                dfs(num + new, new, depth +1)



dfs(start, 0, 0)

print(answer +1)

