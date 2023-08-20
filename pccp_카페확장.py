def solution(menu, order, k):
    import heapq
    import collections
    # 들어온 시간과 나간 시간 배열 만들기
    # 나간 시간 = 들어온 시간 + 음료제조 시간 + 대기시간

    inout = collections.deque()
    n = len(order)

    for i in range(n):
        # print('inout', inout)
        # 들어온 시간 + 음료 제조에 걸린시간
        if len(inout) ==0:
            out = i*k + menu[order[i]]
        else:
            #대기시간 = 가장 최근 사람이 나간시간 - 들어온 시간
            if i*k < inout[-1][1]: # 대기시간 발생
                out = i*k + (inout[-1][1]-i*k) + menu[order[i]]
            else: #대기시간 발생하지 않음
                out = i*k + menu[order[i]]
        inout.append((i*k, out))
    # print('inout', inout)



    # 이제 돌면서 같이 얼마나있는지 확인
    q = [] # 같이 있을수 있는 방
    max_len = 0
    while inout:
        # print("q", q)

        ## 길이 업데이트
        

        start, end = inout.popleft()
        # print("start, end", start, end)
        if len(q) ==0: #그냥 집어넣음
            heapq.heappush(q, end)
        else:
            while q:
                if start >= q[0]: # 시작시간이 끝나는 시간 보다 크면 같이 못있음
                    heapq.heappop(q)
                else: # start < q[0] : 시작시간이 끝나는 시간보다 작으면 같이 있을 수 있음
                    heapq.heappush(q, end)
                    break
            if len(q) ==0:
                heapq.heappush(q, end) #성에 차는 애들이 하나도 없을 경우 시작시간 추가
        
        # 대기열 수 업데이트
        if len(q) > max_len:
            max_len = len(q)
            
    # print("max_len", max_len)
    return max_len


menu = [5, 12, 30]
order = [1, 2, 0, 1]
k = 10
# menu = [5, 12, 30]
# order = [2, 1, 0, 0, 0, 1, 0]
# k = 10
# menu = [5]
# order = [0, 0 ,0 ,0, 0]
k =5

print(solution(menu, order, k))