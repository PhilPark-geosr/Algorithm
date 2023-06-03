import sys
import itertools
sys.stdin = open('input_1759.txt', 'r')
L, C = map(int, input().split())
secret_list = input().split()
print(secret_list)
word_list = ['a', 'e', 'i', 'o', 'u']
secret_list.sort()

for elem in itertools.combinations(secret_list, L):
    word = "".join(elem)
    word_len = len(word)
    count = 0
    for s in word:
        if s in word_list:
            count+=1
    if count >=1 and word_len - count >=2:
        print(word)