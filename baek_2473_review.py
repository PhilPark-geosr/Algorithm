import sys
sys.stdin = open('input_2473.txt', 'r')
# input=sys.stdin.readline


# input
n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

# 함수 정의
def get_min(target, arr):
    n = len(arr)
    min_value = 3*10**9
    l = 0
    r = n-1
    result = []
    while l < r:
        # 갱신 여부
        if abs(target + arr[l] + arr[r]) < min_value:
            min_value = abs(target + arr[l] + arr[r])
            result = [arr[l],arr[r]] # 갱신

        # 포인터 움직이기
        if target + arr[l] + arr[r] >0:
            r -=1
        elif target + arr[l] + arr[r] <0:
            l+=1
        else: # target + arr[l] + arr[r] ==0 :
            return [0, arr[l], arr[r]]
    return [min_value] + result


# 결과 값 도출
global_min_value = 3*10**9
result = []

for i in range(n-2):
    target = liquid[i]
    min_value, l, r = get_min(target, liquid[i+1 :])
    # print(liquid[i+1:])

    if min_value < global_min_value:
        global_min_value = min_value
        result = [target, l,r]


print(result[0], result[1], result[2])

