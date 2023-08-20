import sys
sys.stdin = open('input_2473.txt', 'r')
# input = sys.stdin.readline

# input
n = int(input())
number_list = list(map(int, input().split()))

# numberlist 정렬
number_list.sort()

def get_min(base, arr):
    n = len(arr)
    l = 0
    r = n-1

    #최솟값 정의
    min_value = 2*10**9
    min_l = 0
    min_r = 0
    while l < r :
        # print("l,r", l,r)
        
        # 0인값 --> 최소이므로 바로 탈출
        if base + arr[l] + arr[r] ==0 : 
            return arr[l], arr[r], 0
        # 0보다 작은 값 -> 왼쪽포인터 옮긴다
        if base + arr[l] + arr[r] < 0:
            if abs(base + arr[l] + arr[r])< min_value :
                min_value = abs(base + arr[l] + arr[r])
                min_l, min_r = arr[l], arr[r]
            l +=1
        # 0보다 큰 값 -> 오른쪽 포인터 왼쪽으로 옮긴다
        else:
            if abs(base + arr[l] + arr[r])< min_value:
                min_value = abs(base + arr[l] + arr[r])
                min_l, min_r = arr[l], arr[r]
            r-=1

    return min_l, min_r, min_value
        

        

def solution():
    # 예외처리
    if number_list[0] >0: # 다 양수면
        print(number_list[0], number_list[1], number_list[2])
        return
    if number_list[-1] <0 : #다 음수면
        print(number_list[-3], number_list[-2], number_list[-1])
    
    # 이제 양수 음수 섞여있는 경우
    # 정답도출하기
    global_min_value = 2*10**9
    global_min_l = 0
    global_min_r = 0
    global_base = 0
    for i in range(n-2):
        base = number_list[i]
        # print('base', base)
        temp_list = number_list[i+1:]
        min_l, min_r, min_value = get_min(base, temp_list)
        if min_value < global_min_value:
            global_min_value = min_value
            global_min_l, global_min_r = min_l, min_r
            global_base = base

    # print("global_min_value", global_min_value)
    print(global_base, global_min_l, global_min_r)

solution()