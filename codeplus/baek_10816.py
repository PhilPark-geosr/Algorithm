import sys
sys.stdin = open('input_10816.txt','r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
find_numbers = list(map(int, input().split()))

arr.sort()
def get_lower_bound(elem):
    l = 0
    r = N-1
    answer = -1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] < elem:
            l = mid +1
        elif arr[mid] == elem:
            r = mid -1
            answer = mid
        else:
            r = mid -1
    return answer

def get_upper_bound(elem):
    l = 0
    r = N - 1
    answer = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] < elem:
            l = mid + 1
        elif arr[mid] == elem:
            l = mid + 1
            answer = mid
        else:
            r = mid - 1
    return answer


for elem in find_numbers:
    lower_bound = get_lower_bound(elem)
    upper_bound = get_upper_bound(elem)
    if lower_bound ==-1 or upper_bound ==-1:
        print(0, end = " ")
    else:
        print(upper_bound - lower_bound +1, end = " ")