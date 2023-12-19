import sys
import collections
sys.stdin =open('input_1780.txt', 'r')
N = int(input())
grid= []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)

def check(n, x, y):
    v = grid[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if grid[i][j] !=v:
                return False
    return True

count_dic = collections.defaultdict(int)
def dfs(n, x, y):
    # print(f"dfs{n, x,y, count_dic}")
    if n ==1:
        count_dic[grid[x][y]] +=1
        return
    if check(n, x, y) == True: #다 같은 수 일 경우
        # print('다 같은 수입니다', grid[x][y])
        count_dic[grid[x][y]] += 1
        return
    dfs(n//3, x, y)
    dfs(n//3, x, y + n//3)
    dfs(n//3, x, y+ 2*(n//3))
    dfs(n // 3, x+n // 3, y)
    dfs(n // 3, x+n // 3, y+n // 3)
    dfs(n // 3, x+n // 3, y+2 * (n // 3))
    dfs(n // 3, x+2 * (n // 3), y)
    dfs(n // 3, x+2 * (n // 3), y+n // 3)
    dfs(n // 3, x+2 * (n // 3), y+2 * (n // 3))


dfs(N,0,0)
# print(count_dic)
for elem in [-1,0,1]:
    print(count_dic[elem])
