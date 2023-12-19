import sys
sys.stdin = open('input_2696.txt', 'r')
T = int(input())

for _ in range(T):
    N = int(input())

    if N %2 ==0:
        print(N//2)
    else:
        print(N // 2 +1)
    result = []

    num_list = []
    if N > 10:
        num_of_line = N//10
        if N %10 ==0:
            for _ in range(num_of_line):
                temp = list(map(int, input().split()))
                num_list = num_list + temp
        else:
            for _ in range(num_of_line+1):
                temp = list(map(int, input().split()))
                num_list = num_list + temp

    else:
        temp = list(map(int, input().split()))
        num_list = num_list + temp

    cnt = 0
    for i in range(N):
        result.append(num_list[i])

        if (i+1) %2 == 1: #홀수 일때만
            if cnt!=0 and cnt %10 ==0:
                print()
            result.sort()
            mid = len(result)//2
            print(result[mid], end = " ")
            cnt+=1
        else:
            continue
    print()

