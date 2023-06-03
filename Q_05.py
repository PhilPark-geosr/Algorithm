import sys
import itertools
sys.stdin = open('input_Q_05.txt','r')

N, M= map(int, input().split())
numbers = list(map(int, input().split()))

caselist = list(map(list, itertools.combinations(list(range(N)) ,2)))
print(caselist)
count=0
for case in caselist:
    a = case[0]
    b= case[1]
    if numbers[a] != numbers[b]:
        count+=1

print(count)

