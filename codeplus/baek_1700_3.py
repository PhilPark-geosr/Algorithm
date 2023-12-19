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
for i in range(K):
    elem = order_list[i]
    if elem in q: #이미 큐에 있으면
        count[elem]-=1
        continue
    if len(q) <N:
        q.append(elem)
        count[elem]-=1
        continue
    # if len(q) == N:
    # q안에 앞으로 안나올 애들 있으면 체크하기
    flag = False
    for num in q:
        if count[num] ==0:
            q.remove(num)
            q.append(elem)
            #콘센트 뽑음
            answer +=1
            flag = True
            count[elem]-=1
            break
    if flag is True:
        continue

    latest_idx = -1
    latest_num = -1
    for num in q:
        check_list = order_list[i+1:]
        idx = check_list.index(num) #가장 해당값이 먼저 등장하는 인덱스 구하기
        if idx > latest_idx:
            latest_idx = idx
            latest_num = num
    #latest num 제거
    # print("가장 나중에 등장하는 값", latest_num)
    q.remove(latest_num)
    q.append(elem)
    #콘센트 뽑음
    answer +=1
    count[elem]-=1

print(answer)



# temp = [1, 2, 3, 4, 5]
#
# print(temp[5:])


