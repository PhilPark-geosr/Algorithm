import sys
import collections
sys.stdin = open('input_2015.txt', 'r')

N, K = map(int, input().split())
numlist = list(map(int, input().split()))
numlist.insert(0,0)

p_sum = [0]*(N+1)
for i in range(1, N+1):
    p_sum[i] = p_sum[i-1] + numlist[i] 

# print(numlist, p_sum)

count_dic = collections.defaultdict(int) # 합 기록 배열

count_dic[0] =1

cnt = 0 #몇개 해당되는지
for i in range(1, N+1):

    # Sji == m
    # S[i] - S[j-1] == m
    cnt += count_dic[p_sum[i]-K] #갯수 업데이트
    count_dic[p_sum[i]] +=1 # 합 체크 배열 업데이트

print(cnt)
    






