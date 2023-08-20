import sys
sys.stdin = open('input_1806.txt', 'r')
# input= sys.stdin.readline


# input
N, S = map(int, input().split())
number_list = list(map(int, input().split()))
print("number_list", number_list)

# 부분합 찾기
def find_min_interval(arr:list, target:int):
    n = len(arr)
    l = 0
    r = 0
    # 초기값 설정
    sum_value = arr[0]
    # 최소구간 정의
    min_interval = float('inf')

    while l < n and r < n : 
        if sum_value < S:
            r+=1
            if r > n-1:
                break
            # 값 추가
            sum_value += number_list[r]
        else: # sum_value >=S
            # 구간 갱신
            if r-l < min_interval:
                min_interval = r-l
            # 포인터 이동
            sum_value -= number_list[l]
            l +=1
    
    if min_interval == float('inf'): #최소구간 못찾았으면
        return 0 
    else:
        return min_interval+1
    
print(find_min_interval(number_list, S))
