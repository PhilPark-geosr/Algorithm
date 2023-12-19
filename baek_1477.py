import sys
sys.stdin = open('input_1477.txt', 'r')
N, M, L = map(int, input().split())

numbers = list(map(int, input().split()))


numbers.append(L)
numbers.insert(0,0)
numbers.sort()
# print(numbers)

# d 간격으로 얼마나 휴게소를 세울 수 있는지 체크하는 함수
def build_stop(d):
    cnt = 0
    n = len(numbers)
    if d !=0:
        for i in range(n-1):
            cnt +=(numbers[i+1] - numbers[i]-1)//d
    else:
        cnt = float('inf')

    return cnt

l = 0
r = L
answer = 0
while l<=r:

    mid = (l+r)//2
    # print(mid)
    count = build_stop(mid)

    if count > M: # 더 넓게 간격을 설정해도 된다
        l = mid+1
    else:
        answer = mid
        r = mid-1

print(answer)

# print(0//4)