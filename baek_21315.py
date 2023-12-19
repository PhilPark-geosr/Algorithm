import sys
import itertools
sys.stdin = open('input_21315.txt', 'r')
sys.setrecursionlimit(10**9)

N = int(input())
target = list(map(int, input().split()))

basenum = [i for i in range(1, N+1)]
def oper(k, arr, N):
    result = []
    result = result + [arr[-2 ** 0]]
    # print(arr[-2 ** 0])

    for i in range(1, k+1):
        # print(-2 ** i + 2 ** (i - 1))
        result = result + arr[-2**i : -2**(i-1)]
        # print(arr[-2**i : -2**(i-1)])

    if k < N: #작을때
        result = result + arr[-N : -2**k]
        

    return result

# print(oper(1, basenum, N))
#
# print(oper(3, [1,2,3,4,5,6,7,8]))


# Max k 구하기
def get_max_k(N):
    cnt =0
    while True:
        if 2**cnt > N:
            return cnt-1
        cnt +=1

k = get_max_k(N)
#
base_case = [i for i in range(1, k+1)]
case_list = list(itertools.product(base_case, repeat =2))
# print(case_list)
#
for case in case_list:
    result = oper(case[0], basenum, N)
    result2 = oper(case[1], result, N)

    if result2 == target:
        print(case[0], case[1])
        break