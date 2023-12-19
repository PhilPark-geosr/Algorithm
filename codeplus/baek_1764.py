import sys
sys.stdin = open('input_1764.txt', 'r')

N, M = map(int, input().split())
A = set()
B = set() 
for _ in range(N):
    elem = input()
    A.add(elem)
for _ in range(M):
    elem = input()
    B.add(elem)

C = A & B
C = list(C)
C.sort()
print(len(C))
for elem in C:
    print(elem)