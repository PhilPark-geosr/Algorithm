import sys
sys.stdin  = open('input_12904.txt', 'r')

S = input()
T = input()


n = len(T)
while n> len(S):
    # print("T", T)
    if T[-1] == "A":
        T = T[:n-1]
    else:
        T = T[:n-1]
        T = T[::-1]

    n = n-1

# print("last T", T)

if T == S:
    print(1)
else:
    print(0)