import sys
import collections
sys.stdin = open('Sam의 피자학교.txt', 'r')

input = sys.stdin.readline

n, k = map(int, input().split()) #도우 길이, 최대-최소
dows = list(map(int, input().split()))

#밀가루 넣어주기

def find_min_idx(value):
    result = []
    for i in range(len(dows)):
        elem = dows[i]
        if elem == value:
            result.append(i)
    return result
def add():
    min_value = min(dows)
    idx_list = find_min_idx(min_value)
    for idx in idx_list:
        dows[idx] +=1


def copy(arr):
    result= []
    for i in range(len(arr)):
        result.append(arr[i])
    return result

def rotate(arr):
    rows = len(arr)
    cols = len(arr[0])

    B = [[0]*rows for _ in range(cols)]

    # 행 열 바꿈
    for i in range(rows):
        for j in range(cols):
            B[j][rows-1-i] = arr[i][j]

    return B

def rolling():
    temp = [[dows[0]]]
    copy_dows = copy(dows)#복사
    copy_dows = collections.deque(copy_dows[1:]) #큐로 변환

    while True:
        # print('temp', temp)
        # print('copy_dows', copy_dows)
        l = len(temp) #세로 길이
        if l > len(copy_dows):
            temp[-1] = temp[-1] + list(copy_dows)
            break
        else:
            temp = rotate(temp) #전치 행렬 구함
            result = []
            for _ in range(l): #행길이만큼 뽑아서 밑에 더함
                elem = copy_dows.popleft()
                result.append(elem)
            # 결과 더함
            temp.append(result)

    return temp

# dows = rolling()


# 도우 눌러주기
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def is_range(x,y):
    if x < 0 or y<0 :
        return False
    try:
        elem = dows[x][y]
        # print('elem', elem)
        return True
    except:
        return False

def press():
    #
    def check(x, y):
        # print('dows', dows)
        # if arr[x][y] !=0:
        #     return
        # print(f"check{x,y}, {dows[x][y]}")
        for k in range(4):
            new_x, new_y = x+ dx[k], y +dy[k]

            if is_range(new_x, new_y) == False:
                # print('범위를 벗어납니다')
                continue
            # print("x, y, new_x, new_y", dows[x][y], dows[new_x][new_y])
            div = abs(dows[x][y] - dows[new_x][new_y]) // 5
            # print('몫', div)
            if dows[x][y] > dows[new_x][new_y]:
                # arr[x][y] -= div
                # print(f'arr{new_x, new_y}에 추가합니다')
                arr[new_x][new_y] += div
            else:
                # print(f'arr{x, y}에 추가합니다')
                # arr[x][y] += div
                arr[new_x][new_y] -= div

    # 카피할 도우 만들어주기

    arr = []
    for i in range(len(dows)):
        line = [0]*len(dows[i])
        arr.append(line)
    # print(arr)

    for i in range(len(dows)):
        for j in range(len(dows[i])):
            # elem = dows[i][j]
            check(i,j)
            # print(arr)
    # print(arr)

    #복사
    for i in range(len(dows)):
        for j in range(len(dows[i])):
            dows[i][j] += arr[i][j]

    # print("dows", dows)
# press()

def flatten():
    # 도우 부풀리기
    cols = len(dows[-1]) #밑바닥
    rows = len(dows)
    temp = [[False]*cols for _ in range(rows)]

    for i in range(len(dows)):
        for j in range(len(dows[i])):
            temp[i][j] = dows[i][j]

    #temp를 쭉 핀다
    result = []
    for j in range(cols):
        for i in range(rows-1, -1, -1):
            if temp[i][j] == False:
                continue
            result.append(temp[i][j])
    return result
# dows = flatten() #도우 일자로 피기
# print(dows)

#도우 반으로 접기

def rotate_pi(arr):
    arr = rotate(arr)
    arr = rotate(arr)
    return arr

def cut_half(arr):
    rows = len(arr)
    cols = len(arr[0])//2
    result = [[0]*cols for _ in range(rows)]
    res=  [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = arr[i][j]
            res[i][j] = arr[i][j+cols]
    return result, res


def fold():
    temp = copy(dows)
    temp = [temp]
    for _ in range(2):
        temp, remain = cut_half(temp)
        temp = rotate_pi(temp)
        temp = temp+ remain
    return temp

# dows= fold()
# press()
# dows = flatten()
# print(dows)

cnt = 0 #수행횟수
while True:
    # print('dows', dows)
    # dows의 최대 최소를 계산한다
    min_value, max_value = min(dows), max(dows)

    if max_value - min_value <=k:
        print(cnt)
        break
    # 1번
    add()
    # 2번
    dows = rolling()
    #3번
    press()
    dows = flatten()
    # 4번
    dows = fold()
    # 3번
    press()
    dows = flatten()형
    cnt+=1
    # print("dows", dows)