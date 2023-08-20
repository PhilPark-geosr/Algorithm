import sys
import collections
sys.stdin = open('input_2632.txt', 'r')
#input = sys.stdin.readline

# input
T = int(input())
n, m = map(int, input().split())

# 모든 경우의 수 구하기
# 1. 리스트 만들기
A_list = []
for _ in range(n):
    elem = int(input())
    A_list.append(elem)
B_list = []
for _ in range(m):
    elem = int(input())
    B_list.append(elem)

# 2. 경우의 수 기록하기
case_A = collections.defaultdict(int)
case_B = collections.defaultdict(int)

# 경우의 수 만드는 함수
def make_case(arr:list, dic:dict):
    # 전체 다 더한거 기록
    total_sum = sum(arr)
    dic[total_sum] +=1
    n = len(arr)
    arr_deq= collections.deque(arr) # 큐로 변환

    for _ in range(n) : #n-1번 돌리면서 다 기록할거임

        # 부분합 구하기
        sum_value = 0
        for i in range(n-1): #하나 전까지만 기록
            sum_value +=arr_deq[i]
            dic[sum_value] +=1 # 경우의 수 기록
        
        # 다 기록했으면, 하나씩 옮기기
        a = arr_deq.popleft()
        arr_deq.append(a) 
    return dic

# test
case_A = make_case(A_list, case_A)
case_B = make_case(B_list, case_B)
# print('case_A', case_A)
# print('case_B', case_B)


# 숫자 카운트 하기
cnt = 0
for i in range(T+1):
    # 둘다 존재하면 곱하고
    # print('i', i)
    if case_A[i]!=0 and case_B[T-i]!=0:
        # print(case_A[i], case_B[T-i])
        cnt += case_A[i]*case_B[T-i]
cnt += case_A[T]
cnt += case_B[T]
print(cnt)
