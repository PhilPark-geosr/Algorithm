import sys
import copy
sys.stdin = open('input_12100.txt', 'r')
N = int(input())

base_grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    base_grid.append(line)

# test
# N = 4
# grid = [[2, 0,0,0], [2,2,0,0], [2,0,0,0], [0,0,0,0]]
# grid = [[0, 0,2,0], [0,0,0,0], [2,0,0,0], [0,0,0,0]]
# grid = [[4, 2,0,0], [0,0,0,0], [0,0,0,0], [2,0,0,0]]
# grid = [[2, 0,2,8], [0,0,2,2], [0,0,0,0], [0,0,0,0]]
# grid = [[2, 4,16,8], [8,4,0,0], [16,8,2,0], [2,8,2,0]]
# print('초기',grid)
def go_up(grid):
    check = [[0]*N for _ in range(N)]

    def up(i, j):
        while i > 0:
            if grid[i-1][j] == 0:
                grid[i-1][j] = grid[i][j]
                grid[i][j] = 0
                i -= 1
            else:
                if grid[i-1][j] == grid[i][j]:
                    if check[i-1][j] != 1:
                        grid[i-1][j] = 2 * grid[i-1][j]
                        grid[i][j] = 0
                        check[i-1][j] = 1
                    break
                else:
                    break

    for i in range(1, N):
        for j in range(N):
            up(i, j)
def go_down(grid):
    check = [[0]*N for _ in range(N)]

    def down(i, j):
        while i < N - 1:
            if grid[i+1][j] == 0:
                grid[i+1][j] = grid[i][j]
                grid[i][j] = 0
                i += 1
            else:
                if grid[i+1][j] == grid[i][j]:
                    if check[i+1][j] != 1:
                        grid[i+1][j] = 2 * grid[i+1][j]
                        grid[i][j] = 0
                        check[i+1][j] = 1
                    break
                else:
                    break

    for i in range(N - 1, -1, -1):
        for j in range(N):
            down(i, j)

def go_left(grid):
    check = [[0]*N for _ in range(N)]

    def left(i, j):
        while j > 0:
            if grid[i][j-1] == 0:
                grid[i][j-1] = grid[i][j]
                grid[i][j] = 0
                j -= 1
            else:
                if grid[i][j-1] == grid[i][j]:
                    if check[i][j-1] != 1:
                        grid[i][j-1] = 2 * grid[i][j-1]
                        grid[i][j] = 0
                        check[i][j-1] = 1
                    break
                else:
                    break

    for j in range(1, N):
        for i in range(N):
            left(i, j)

def go_right(grid):
    check = [[0]*N for _ in range(N)]

    def right(i, j):
        while j < N - 1:
            if grid[i][j+1] == 0:
                grid[i][j+1] = grid[i][j]
                grid[i][j] = 0
                j += 1
            else:
                if grid[i][j+1] == grid[i][j]:
                    if check[i][j+1] != 1:
                        grid[i][j+1] = 2 * grid[i][j+1]
                        grid[i][j] = 0
                        check[i][j+1] = 1
                    break
                else:
                    break

    for j in range(N - 1, -1, -1):
        for i in range(N):
            right(i, j)


# go_up(grid)
# print(grid)
# go_left(grid)
# print(grid)

# go_right(grid)
# print(grid)
# go_up(grid)
# print(grid)
# go_right(grid)
# print(grid)

# go_left(grid)
# print(grid)

# go_up(grid)
# print(grid)

caselist = [go_up, go_down, go_left, go_right]

import itertools
caselist = list(map(list, itertools.product(caselist,repeat=5)))
# print(len(caselist))


def get_max_value(grid):
    result = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] > result:
                result = grid[i][j]

    return result


answer = 0
for case in caselist:
    grid = copy.deepcopy(base_grid)
    # print(grid)
    # print("case", case)
    for func in case:
        # print('func', func)
        func(grid)
    
    # print(grid)
    max_value = get_max_value(grid)
    # print(max_value)
    if max_value > answer:
        answer = max_value


print(answer)