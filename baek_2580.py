import sys
sys.stdin = open('input_2580.txt', 'r')
input = sys.stdin.readline
# input
grid = []
for _ in range(9):
    line = list(map(int, input().split()))
    grid.append(line)

def check(): #전체다 0하나도 없는지 체크
    cnt = 0
    for i in range(9):
        for j in range(9):
           if grid[i][j] == 0:
               cnt+=1

    if cnt == 0:
        return True
    else:
        return False

# 행렬 출력
def print_arr():
    for i in range(9):
        line = grid[i]
        for j in range(9):
            print(line[j], end = " ")
        print()

def fill_block(arr):
    ch = [0]*10 #체크배열 선언
    cnt = 0 #0 갯수 세기
    for i in range(3):
        for j in range(3):
            value = arr[i][j]
            if value ==0:
                cnt +=1
            ch[value] = 1
    
    if cnt == 1: # 채울수 있는경우
        fill_value = -1
        for k in range(1, 10):
            if ch[k] == 0:
                fill_value = k
        # fill_value 채우기
        for i in range(3):
            for j in range(3):
                value = arr[i][j]
                if value == 0: #0인곳에
                    arr[i][j] = fill_value
    return arr

def proc_block():
    case = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
    for x, y in case:
        temp = [[0]*3 for _ in range(3)] # 3X3 만들기
        for i in range(3):
            for j in range(3):
                temp[i][j] = grid[x+i][y+j]

        # 체크해서 채워넣을수 있으면 채워넣기
        new_temp = fill_block(temp)

        for i in range(3):
            for j in range(3):
                grid[x+i][y+j] = new_temp[i][j]


def fill_row(arr):
    # 0이 1개인지 체크
    ch = [0]*10
    cnt = 0
    for i in range(9):
        if arr[i] == 0:
            cnt += 1
        ch[arr[i]] =1

    if cnt ==1 : #채울 수 있을때
        fill_value = -1
        for i in range(1, 10):
            if ch[i] == 0:
                fill_value = i

        for i in range(9):
            if arr[i] == 0:
                arr[i] = fill_value
    return arr


def proc_row():
    for i in range(9):
        row = grid[i]
        new_row = fill_row(row)
        grid[i] = new_row



def extract_col(i):
    result = []
    for j in range(9):
        result.append(grid[j][i])
    return result
def proc_col():
    for i in range(9):
        col = extract_col(i)
        new_col = fill_row(col)
        for j in range(9):
            grid[j][i] = new_col[j]




#
# proc_block()
# print_arr()



#----------------- Main -----------------------#
while True:
    if check() == True:
        print_arr()
        break
    else:
        proc_row()
        proc_col()
        proc_block()

