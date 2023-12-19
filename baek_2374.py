import sys
sys.stdin = open('input_2374.txt', 'r')
input = sys.stdin.readline
N = int(input())

num_list = []
for _ in range(N):
    elem = int(input())
    num_list.append(elem)

# print("숫자압축전", num_list)
# 숫자 압축

def compress(arr):
    n = len(arr)
    prev = arr[0]
    result = [prev]

    for i in range(1, n):
        cur = arr[i]
        if cur != prev:
            result.append(cur)
        prev = cur
    return result
num_list = compress(num_list)
# print("숫자압축 후", num_list)




# num_list = [10, 5, 1, 3, 2]
# num_list = [1,5,10]


cnt = 0
while len(num_list) > 1:
    # print(num_list)
    n = len(num_list)
    min_value = min(num_list)
    idx = num_list.index(min_value)
    if idx ==0:
        cnt += num_list[idx+1] - num_list[idx]
    elif idx == n-1:
        cnt += num_list[idx-1] - num_list[idx]
    else:
        cnt += min(num_list[idx+1],num_list[idx-1]) - num_list[idx]

    num_list.pop(idx)

print(cnt)
