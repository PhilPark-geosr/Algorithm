import sys
sys.stdin = open('input_11399.txt', 'r')

N = int(input())
line_list = list(map(int, input().split()))

# 정렬
line_list.sort(reverse= True)

answer = 0
for i in range(N):
    answer += (i+1)*line_list[i]

print(answer)