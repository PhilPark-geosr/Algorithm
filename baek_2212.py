import sys
sys.stdin = open('input_2212.txt', 'r')

N = int(input())
K = int(input())
line_list = list(map(int, input().split()))
line_list.sort()
diff = []
for i in range(1, N):
    diff.append(line_list[i] - line_list[i-1])

diff.sort()
# print(diff)

while diff and K-1>0:
    diff.pop()
    K-=1

print(sum(diff))