import sys
sys.stdin =open('input_1654.txt','r')
input = sys.stdin.readline
K, N = map(int, input().split())
MAX_NUM = 2**31 -1
lans = []
for _ in range(K):
    elem = int(input())
    lans.append(elem)

def get_num_of_lans(arr, x):
    cnt =0
    for elem in arr:
        cnt += elem//x
    return cnt

def binary_search():
    l = 0
    r = MAX_NUM
    answer =-1
    while l<=r:
        mid = (l+r)//2
        cnt = get_num_of_lans(lans, mid)
        if cnt >= N: # 목표한 갯수보다 더 많이 자를 수 있을때
            l = mid +1
            answer =mid
        else:
            r =mid -1
    return answer

answer = binary_search()
print(answer)