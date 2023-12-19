import sys
import itertools
sys.stdin = open('input_20366.txt', 'r')
N= int(input())
num_list = list(map(int, input().split()))

case_list = list(map(list, itertools.combinations([i for i in range(N)], 2)))

# print(case_list)
# print(case_list)

filtered_list = []
for case in case_list:
    filtered_list.append((num_list[case[0]] + num_list[case[1]], case[0], case[1])) #인덱스 까지 기록

# print(filtered_list)
filtered_list.sort()
# print(filtered_list)
answer = 10**9
n = len(filtered_list)
for i in range(n-1):
    val1, x1,y1 = filtered_list[i+1]
    val2, x2,y2 = filtered_list[i]
    if x1 == x2 or x1 == y2 or y1 == x2 or y1 == y2:
        continue
    diff = val1 -val2
    answer = min(diff, answer)

print(answer)

# case_list2 = list(map(list, itertools.combinations(filtered_list, 2)))
#
# answer =10**9
# for case in case_list2:
#     answer = min(abs(case[1]- case[0]), answer)


