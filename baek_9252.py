import sys
import itertools
import collections
sys.stdin = open('input_9252.txt', 'r')

str1 = input()
str2 = input()

# dp 정의
# dp[i][j] # str1의 1~ i번재까지 글자와 str2의 1~j까지 글자로 만들 수 있는 최장 공통 부분 수열 길이

n = len(str1)
m = len(str2)

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if str1[i-1] == str2[j-1] : #맨 마지막 글자가 같으면 최장 공통 부분 수열엔 하나 추가 됨
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i-1][j] ,dp[i][j-1])
max_value = dp[n][m]

## 메모리초과 모드
# if max_value ==0:
#     print(0)
# else:
# # 가장 먼저 max_value 나오는 지점 추출
#     s1 = []
#     s2 = []
#     flag = False
#     for i in range(1, n+1):
#         for j in range(1, m+1):
#             if dp[i][j] == max_value:
#                 # print(i,j)
#                 s1 = str1[:i]
#                 s2 = str2[:j]
#                 flag = True
#                 break
#         if flag == True:
#             break
#     len_s1= len(s1)


#     # 경우의 수 따지기
#     caselist = list(range(len_s1))
#     caselist = list(map(list,itertools.combinations(caselist, max_value)))
#     # print(caselist)
#     for case in caselist:
#         q = collections.deque()
#         case_str = ""
#         # q 생성
#         for elem in case:
#             q.append(s1[elem])
#             case_str += s1[elem]
#         for s in s2:
#             if q[0] ==s:
#                 q.popleft()
#         if len(q) ==0:
#             break
#     print(max_value)
#     print(case_str)

# 역추적
x = n
y = m
answer =""
while x >0 and y>0:
    # print(x,y ,dp[x][y])
    left = dp[x][y-1]
    up = dp[x-1][y]

    if dp[x][y] == left:
        y = y-1
    elif dp[x][y] == up:
        x = x-1
    else: 
        answer+=str1[x-1]
        x = x-1
        y = y-1
print(max_value)
if len(answer) !=0:
    answer = answer[::-1]
    print(answer)