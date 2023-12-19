import sys
sys.stdin = open('input_22945.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))

l = 0
r = N-1
answer =0
while l<=r:
    answer  = max(answer, min(arr[l], arr[r])*(r-l-1))

    if arr[l] < arr[r]:
        l +=1
    else:
        r -=1

print(answer)