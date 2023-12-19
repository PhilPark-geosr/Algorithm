import sys
sys.stdin = open('input_14500.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)


def check_pos(i,j, case): #O(4)
    for x,y in case:
        if x+i <0 or x+i >N-1 or y+j <0 or y+j > M-1:
            return False #하나라도 안되면
        
    return True

def get_sum(i,j, case):
    result = 0
    for x,y in case:
        new_x, new_y = x + i, y+j
        result += grid[new_x][new_y]
    return result

# caselist 만들기
caselist = [[(0,0), (0,1), (0,2), (0,3)], [(0,0), (1,0), (2,0), (3,0)], \
            
            [(0,0), (0,1), (1,0), (1,1)], \
            
            [(0,0), (1,0), (2,0), (2,1)], [(0,0), (0,1), (0,2), (1,0)],\
            [(0,0), (0,1), (1,1), (2,1)], [(0,0), (0,1), (0,2), (-1,2)],\
            [(0,0), (0,1), (-1,1), (-2,1)], [(0,0), (0,1), (1,0), (2,0)],\
            [(0,0), (0,1), (0,2), (1,2)], [(0,0), (1,0), (1,1), (1,2)], 
            
            [(0,0), (1,0), (1,1), (2,1)], [(0,0), (0,1), (-1,1), (-1,2)], \
            [(0,0), (0,1), (1,1), (1,2)],  [(0,0), (1,0), (0,1), (-1,1)],

            [(0,0), (0,1), (0,2), (1,1)], [(0,0), (0,1), (-1,1), (1,1)],\
            [(0,0), (0,1), (0,2), (-1,1)], [(0,0), (1,0), (2,0), (1,1)]
            ]

# test
# case = [(0,0), (0,1), (0,2), (0,3)]
max_value = 0
for case in caselist: # O(19)
    # print(case)
    for i in range(N):
        for j in range(M):
            if check_pos(i,j, case) == False: #O(4)
                # print('여기에 위치할 수 없습니다', i,j)
                continue
            value = get_sum(i,j, case) #O(4)
            # print(value, i,j)
            max_value = max(value, max_value)

# O(N*M*4*19) = 500*500 = 250000
print(max_value)