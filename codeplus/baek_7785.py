import sys
sys.stdin = open('input_7785.txt', 'r')
input =sys.stdin.readline
N = int(input())

dic = dict()

for _ in range(N):
    name, check = input().split()
    dic[name] = check

# print('dic', dic)

result = []
for key in dic:
    if dic[key] == "enter":
        result.append(key)

result.sort(reverse = True)

for elem in result:
    print(elem)