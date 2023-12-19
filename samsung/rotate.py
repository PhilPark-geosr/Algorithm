arr = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

def rotate(arr):
    rows = len(arr)
    cols = len(arr[0])
    new_arr = [[0]*rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            new_arr[j][rows-i-1] = arr[i][j]
    return new_arr

# print(rotate(arr))

def rotate_reverse_90(arr):
    rows = len(arr)
    cols = len(arr[0])
    new_arr = [[0]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            new_arr[cols-1-j][i] = arr[i][j]
    return new_arr
#
# print(rotate_reverse_90(arr))

def rotate_180(arr):
    rows = len(arr)
    cols = len(arr[0])
    new_arr = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            new_arr[rows - 1 - i][cols-1-j] = arr[i][j]
    return new_arr
#
# print(rotate_180(arr))

# 7X7 배열
arr = [[7 * j + i for i in range(1, 8)] for j in range(7)]
new_arr = [[0] * 7 for _ in range(7)]
sy, sx = 2, 2
length = 3

def rotate_part(sx,sy, n_rows, n_cols): #직사각형 부분회전
    new_arr = [[0]*(n_cols) for _ in range(n_rows)]
    for i in range(sx, sx+n_rows):
        for j in range(sy, sy+n_cols):
            new_arr[i-sx][j-sy] = arr[i][j]
    #90도 회전
    print(new_arr)
    new_arr = rotate(new_arr)
    print(new_arr)
    #옮기기
    for i in range(sx,sx+n_rows):
        for j in range(sy, sy+n_cols):
            arr[i][j]= new_arr[i-sx][j-sy]

rotate_part(2,2,3,3)
print(arr)


print(arr)