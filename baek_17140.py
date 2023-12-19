import sys
import heapq
import collections
sys.stdin = open('input_17140.txt', 'r')
input = sys.stdin.readline

r, c, k = map(int, input().split())
arr = []
for _ in range(3):
    line = list(map(int, input().split()))
    arr.append(line)

def convert(line): # 정렬하는 함수
    result = []
    count_dic = collections.defaultdict(int)
    for elem in line:
        if elem == 0: #0이 있으면 무시
            continue
        count_dic[elem] +=1
    q = []
    for key in count_dic:
        heapq.heappush(q, (count_dic[key], key))

    while q:
        cnt, num = heapq.heappop(q)
        result.append(num)
        result.append(cnt)

    return result
def oper_r(arr):
    # max_length 갱신
    temp_arr = []
    max_length = 0
    for line in arr:
        # print(line)
        new_line = convert(line)[:101]
        max_length = max(max_length, len(new_line))
        temp_arr.append(new_line)
    # 빈칸 채우기
    # print(temp_arr)
    new_arr = []
    for line in temp_arr:
        if len(line) < max_length:
            res = [0 for _ in range(max_length - len(line))]
            new_line = line + res
            new_arr.append(new_line)
        else:
            new_arr.append(line)
    # print("new_arr", new_arr)
    return new_arr



def oper_c(arr):
    m = len(arr[0])
    n = len(arr)
    temp_arr = []
    max_length = 0
    for j in range(m):
        line = []
        for i in range(n):
            line.append(arr[i][j])
        new_line = convert(line)[:101]
        max_length = max(max_length, len(new_line))
        temp_arr.append(new_line)
    # print(temp_arr)
    # 채우기
    new_arr = [[0]*m for _ in range(max_length)]
    # print(new_arr)
    for i in range(m):
        line = temp_arr[i]
        if len(line) < max_length:
            res = [0 for _ in range(max_length - len(line))]
            new_line = line + res
        else:
            new_line = line

        for j in range(len(new_line)):
            new_arr[j][i] = new_line[j]
    # print(new_arr)
    return new_arr



# test
# oper_r(arr)
# oper_c(arr)

def is_range(x, y, N, M):
    if 0<=x<N and 0<=y<M:
        return True
    return False

t = 0
while True:
    # print(arr[r-1][c-1])
    # print(arr)
    n = len(arr)
    m = len(arr[0])
    # print(n, m)
    #
    if t>100:
        print(-1)
        break
    if is_range(r-1, c-1, n, m) == False:
        pass
    elif arr[r-1][c-1] == k:
        print(t)
        break

    # print(n,m)

    if n >= m:
        # print('R연산')
        arr = oper_r(arr)
    else:
        arr = oper_c(arr)
    t +=1