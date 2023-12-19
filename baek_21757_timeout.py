import sys
sys.stdin = open('input_21757.txt', 'r')

N = int(input())
num_list = list(map(int, input().split()))

def get_partial_sum(arr):
    n = len(arr)
    s = [0]*(n+1)
    # s[i] - s[i-1]
    for i in range(1, n+1):
        s[i] = s[i-1] + arr[i-1]
    return s

p_sum = get_partial_sum(num_list)
print(p_sum)

answer = 0
for i in range(1, N+1):
    base= p_sum[i]
    candidates = [4*base, 3*base, 2*base]
    flag = False
    for j in range(i,N+1):
        if len(candidates) == 0:
            flag = True
            break
        target = candidates[-1]
        if p_sum[j] == target:
            candidates.pop()

    if len(candidates) == 0:
        flag = True

    # 처리되었는지 확인
    if flag == True:
        print(base)
        answer +=1

print(answer)



