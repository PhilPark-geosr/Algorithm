import sys
sys.stdin = open('input_2217.txt', 'r')
import collections
n = int(input())

ropelist = []
for _ in range(n): #O(n)
    elem = int(input())
    ropelist.append(elem)

ropelist.sort() #O(nlogn)

dic = collections.Counter(ropelist)
# print(dic)

keylist = list(dic.keys())
keylist.sort()

total_weight = 0
num_of_ropes = n #처음 n개
for key in keylist:
    temp_weight = key*num_of_ropes
    # print(temp_weight, num_of_ropes, key)
    num_of_ropes = num_of_ropes - dic[key]
    if temp_weight>total_weight:
        total_weight = temp_weight
print(total_weight)

