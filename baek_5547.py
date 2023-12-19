import sys
import collections
sys.stdin = open('input_5547.txt', 'r')
input = sys.stdin.readline

W, H = map(int, input().split())
grid = [[0]*(W+2)]
for _ in range(H):
    line =[0]  + list(map(int, input().split())) + [0]
    grid.append(line)
grid.append([0]*(W+2))
# print(grid)

def is_range(x,y):
    if 0<=x<=H+1 and 0<=y<=W+1:
        return True
    return False


def bfs(start_x, start_y):
    visited = [[0] * (W + 2) for _ in range(H + 2)]  # 방문 기록
    answer = 0  # 닿는 면적의 갯수
    q = collections.deque()
    visited[start_x][start_y] = 1
    q.append((start_x, start_y))
    while q:
        x,y = q.popleft()

        if x % 2 == 1:  # 홀수
            dx = [-1, -1, 0, 0, 1, 1]
            dy = [1, 0, -1, 1, 0, 1]

        else:
            dx = [-1, -1, 0, 0, 1, 1]
            dy = [0, -1, -1, 1, -1, 0]

        for k in range(6):
            new_x, new_y = x + dx[k], y + dy[k]
            # print(new_x, new_y)

            if is_range(new_x, new_y) == True and visited[new_x][new_y] == 0:

                if grid[new_x][new_y] ==1:
                    answer+=1
                else:
                    # 집이 아닌곳만 방문처리를 하는 것이 핵심이다!
                    visited[new_x][new_y] = 1
                    q.append((new_x, new_y))
    return answer


print(bfs(0,0))






