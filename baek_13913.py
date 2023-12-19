import sys
import collections
sys.stdin = open('input_13913.txt', 'r')
input = sys.stdin.readline
start, end = map(int, input().split())

path = [-1]*(100001)

def bfs(start, end):
    q = collections.deque()
    visited = [0]*(100001)
    distance = [0]*(100001)
    q.append((start, 0))
    visited[start] =1
    distance[start] = 0

    while q:
        now, time= q.popleft()
        if now == end:
            # return time
            break
        for node in [now-1, now+1, 2*now]:
            new_time = time+1
            if 0<=node<=100000 and visited[node] ==0:
                distance[node] = new_time
                path[node] = now
                visited[node] = 1

                q.append((node, new_time))
    return distance


result = bfs(start, end)
print(result[end])
# print(path)
answer = []
node = end
while node:

    # print(node)
    answer.append(node)
    if node == start:
        break
    node = path[node]


# print(answer)
for i in range(len(answer)-1, -1, -1):
    print(answer[i], end =" ")



