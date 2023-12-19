import sys
sys.stdin = open('input_13397.txt')

N, M = map(int, input().split())
arr = list(map(int, input().split()))
max_num = 10**4-1


def can_make(x):
    min_v = float('inf')
    max_v = 0
    cnt = 1
    for i in range(N):
        # print(min_v, max_v)
        elem = arr[i]


        if elem < min_v:
            min_v = elem
        if elem > max_v:
            max_v = elem

        if max_v-min_v <=x:
            continue
        else:
            max_v = elem
            min_v = elem
            cnt +=1
    # print(cnt)
    if cnt <=M:
        return True
    return False




l = 0
r = max_num
answer = -1
while l<=r:
    mid =(l+r)//2
    if can_make(mid) == True:
        r = mid -1
        answer = mid
    else:
        l = mid +1
print(answer)