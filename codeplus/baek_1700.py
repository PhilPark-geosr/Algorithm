import sys
import heapq
import collections
sys.stdin = open('input_1700.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
order_list = list(map(int, input().split()))

q = []
# 몇개 남아있는지 카운트
count = collections.defaultdict(int)
for elem in order_list:
    count[elem] +=1
# print(count)

concent_dic = dict()

answer = 0
for elem in order_list:
    # print(concent_dic, q)
    if len(q) <N:
        count[elem] -=1
        heapq.heappush(q, (count[elem], elem))
        concent_dic[elem]= True

    else: # len(q) == N

        # 이미 있는 자료의 경우
        if elem in concent_dic:
            continue # 안뺀다
        else:
            # 가장 적게 남은 애를 뺸다
            cnt, num = heapq.heappop(q)
            concent_dic.pop(num, None)
            count[elem] -= 1
            heapq.heappush(q, (count[elem], elem))
            answer +=1
            concent_dic[elem] = True

# print(concent_dic)
print(answer)

