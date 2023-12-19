import sys
sys.stdin = open('input_1074.txt', 'r')
sys.setrecursionlimit(10**9)
N, r, c = map(int, input().split())

# grid =[[0]*(2**N+1) for _ in range(2**N+1)]

global cnt
def dfs(n, i, j):
    # print(f"dfs{n, i,j}")
    global cnt
    if n ==0:
        if (i,j) == (r+1, c+1):
            print(cnt)
        # grid[i][j] = cnt
        cnt +=1
        return
    dfs(n - 1 , i, j)
    dfs(n - 1, i, j + 2**(n-1))
    dfs(n - 1, i + 2 ** (n - 1), j)
    dfs(n - 1, i + 2 ** (n - 1), j + 2**(n-1))



cnt = 0
dfs(N, 1, 1)
# print(grid)
# print(grid[r+1][c+1])