import sys
sys.stdin = open('input_2343.txt', 'r')
N, M = map(int, input().split())
numlist = list(map(int, input().split()))
max_size = (10**5)*(10**4)


def make_blueray(arr, size):
    tot = 0
    cnt =1
    n = len(arr)
    for i in range(n):
        if arr[i] > size:
            return max_size
        if tot + arr[i] > size:
            cnt += 1
            tot = arr[i]
        else:
            tot += arr[i]
    return cnt


# print(make_blueray(numlist, 16))

answer = max_size
l = 0
r = max_size
while l<=r:
    mid =(l+r)//2
    cnt = make_blueray(numlist, mid) # 해당 크기로 테잎 담아본다
    # print('cnt',cnt, mid)
    if cnt > M:
        l = mid +1
    else:
        r = mid -1
        answer = mid

print(answer)
