import sys

sys.stdin = open('input_18310.txt', 'r')

N = int(input())
l = 0
r = N-1
mid = (l+r)//2
poslist = list(map(int, input().split()))
poslist.sort()
# print(poslist)
print(poslist[mid])
