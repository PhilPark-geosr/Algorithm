import sys
sys.stdin = open('input_12919.txt', 'r')
sys.setrecursionlimit(10**9)
target = input()
S = input()


def dfs(S, target):
    # print(f"dfs{S, target}")

    if len(S) ==1:
        if S == target:
            return True
        else:
            return False
        
    if S == target:
        return True
    check1, check2 = False, False
    if S[-1] == "A":
        check1 = dfs(S[:-1], target)
    if S[0] == "B":
        S = S[1:]
        S = S[::-1]
        check2 = dfs(S, target)

    if check1 == True or check2 == True:
        return True
    return False
    
if dfs(S, target):
    print(1)
else:
    print(0)
