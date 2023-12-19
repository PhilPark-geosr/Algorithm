import sys
import heapq
import collections
sys.stdin = open('input_1700.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
order_list = list(map(int, input().split()))

q = []
# 몇개 남아있는지 카운트
count = [0]*(K+1)
for elem in order_list:
    count[elem] +=1
#print(count)


answer = 0
for elem in order_list:
    print(q, count)
    if len(q) <N:
        q.append(elem)
        count[elem] -=1

    else: # len(q) == N
        # 이미 있는 자료의 경우
        if elem in q:
            count[elem] -=1
            continue # 안뺀다
        else:
            #최솟값 찾기
            min_count = float('inf')
            min_value = float('inf')
            for num in q:
                if count[num] < min_value:
                    min_count = count[num]
                    min_value = num
            # 최솟값인 애 뺀다
            print("min_value", min_value)
            q.remove(min_value)

            # 새로운 원소 콘센트에 집어넣는다
            q.append(elem)
            count[elem] -=1

            # 콘센트 뽑는 횟수 추가한다
            answer +=1

print(answer)
# # print(concent_dic)
# print(answer)
#
