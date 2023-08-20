import sys
sys.stdin = open('input_12378.txt', 'r')

N = int(input())
numlist = list(map(int, input().split()))

def find_lower_bound(result, elem):
    n = len(result)
    l = 0
    r = n-1
    answer = n-1
    while l<=r:
        mid = (l+r)//2

        if result[mid]< elem:
            l = mid+1
        else:
            if mid < answer:
                answer = mid
            r = mid -1

    return answer




result = []
for elem in numlist:
    # print(result)
    if len(result) ==0:
        result.append(elem)
        continue
    if elem > result[-1]: #가장 큰수보다 크면 일단 추가
        result.append(elem)
    else:
        idx = find_lower_bound(result, elem)
        #  ('idx', idx)
        result[idx] = elem

print(len(result))
