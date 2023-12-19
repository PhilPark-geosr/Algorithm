import sys
sys.stdin =open('input_20444.txt','r')

N, K = map(int, input().split())


flag = False

# ''' 시간초과 풀이 '''
# for x in range(N+1):
#     # print(f"(x+1)*(N-x+1)", (x+1)*(N-x+1))
#     if (x+1)*(N-x+1) == K:
#         flag= True
#         break


l = 0
r = N
while l<=r:
    x = (l+r)//2
    if (x+1)*(N-x+1) -K <0:
        l = x+1
    elif (x+1)*(N-x+1) -K == 0:
        flag =True
        break
    else:
        r = x-1

if flag ==True:
    print('YES')
else:
    print('NO')