import sys
sys.stdin = open('input_1074.txt', 'r')
sys.setrecursionlimit(10**9)
N, r, c = map(int, input().split())

# grid =[[0]*(2**N+1) for _ in range(2**N+1)]
def check_area(N, i, j): #i,j가 2^N 2^N에서 어디사분면에 있는지
    if 0<=i<2**(N-1) and 0<=j<2**(N-1):
        return 0
    if 0<=i<2**(N-1) and 2**(N-1)<=j<2**N:
        return 1
    if 2**(N-1)<=i<2**N and 0<=j<2**(N-1):
        return 2
    else:
        return 3

def dfs(N, i, j, start):
    # print(f'dfs{N, i, j, start}')
    if N==1:
        if (i,j) == (0,0):
            print(start)
        elif (i,j) == (0,1):
            print(start+1)
        elif (i,j) == (1,0):
            print(start+2)
        elif (i,j) == (1,1):
            print(start+3)
        return


    area = check_area(N, i, j)
    # print(f"{i,j}는 {area} 사분면에 있습니다")
    if area == 0:
        dfs(N-1, i, j, start)
    elif area == 1:
        dfs(N-1, i, j-2**(N-1), start + area*2**(2*N-2))

    elif area ==2:
        dfs(N - 1, i - 2 ** (N - 1), j , start + area * 2 ** (2*N-2))

    else:
        dfs(N - 1, i - 2 ** (N - 1), j- 2 ** (N - 1), start + area * 2 ** (2*N-2))


dfs(N, r, c, 0)
