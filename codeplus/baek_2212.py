import sys
import heapq
sys.stdin = open('input_2212.txt', 'r')
input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))

sensors.sort()
diff = []
for i in range(N-1):
    heapq.heappush(diff, -(sensors[i+1] - sensors[i]))
# print("diff", diff)
cnt =0
while diff and cnt < K-1:
    heapq.heappop(diff)
    cnt+=1
# print(diff)
if len(diff) ==0:
    print(0)
else:
    print(-sum(diff))
