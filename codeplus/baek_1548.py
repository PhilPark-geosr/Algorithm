import sys
import collections
sys.stdin= open('input_1548.txt', 'r')

N = int(input())
numbers = list(map(int, input().split()))
q = collections.deque()

numbers.sort()
max_len = 0
for elem in numbers:
    # print(q)
    if len(q) < 2:
        q.append(elem)
    else:
        while q:
            if len(q) <2:
                break
            if elem < q[0] + q[1]:
                break
            q.popleft()
        q.append(elem)

    # max_len 갱신
    max_len = max(max_len, len(q))

# print(q)
print(max_len)