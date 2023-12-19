arr =[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

def copy(arr):
    n, m = len(arr), len(arr[0])
    new_arr = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_arr[i][j] = arr[i][j]
    return new_arr

def fluid():
    # new_arr 카피
    n = len(arr)
    new_arr = copy(arr)

    # 맨 위 옮기기
    for i in range(4):
        new_arr[0][i+1] = arr[0][i]
    # 오른쪽
    for i in range(4):
        new_arr[i+1][4] = arr[i][4]

    # 아래
    for i in range(4):
        new_arr[4][i] = arr[4][i+1]

    # 왼쪽
    for i in range(4):
        new_arr[i][0] = arr[i+1][0]

    #다시 정보 옮겨주기
    for i in range(n):
        for j in range(n):
            arr[i][j] = new_arr[i][j]

fluid()
print(arr)