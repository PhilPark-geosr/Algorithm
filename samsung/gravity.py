arr = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]]
def gravity():
    n = len(arr)
    m = len(arr[0])
    for i in range(n-1):
        for j in range(m):
            p = i
            while p>=0 and arr[p][j] == 1 and arr[p+1][j] == 0:
                arr[p+1][j], arr[p][j] = arr[p][j], arr[p+1][j]
                p-=1
print('org', arr)
gravity()
print(arr)