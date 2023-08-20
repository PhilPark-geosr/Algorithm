def solution(program):
    import collections
    import heapq

    q1 = [] # 호출시간 큐
    q2 = [] # 작업 큐
    waiting_time = [0]*11

    #호출 시간 큐 만들기
    for s, c, w in program:
        q1.append([c,s,w])
    # 호출 시간 순으로 정렬 2순위는 프로그램 점수
    q1.sort(key = lambda x: (x[0], x[1]))
    q1 = collections.deque(q1)

    next_start = 0 #다음 작업이 수행될 수 있는 시간 
    while q1 or q2 : #둘다 빌때까지 수행

        # 작업큐가 비어있으면.. 
        # case1 : 시작할떄
        # case2 : 호출시간큐에 남아있는 작업들의 시작시간이 다음 시작시간보다 클 때
        if len(q2) ==0:
            # 그냥 꺼낸다
            c, s, w = q1.popleft()
            # 이미 c > next_start 이므로 next_start = c로 갱신하고, 대기시간은 없다!
            next_start = c
            heapq.heappush(q2, (s, c, w))
        
        # 작업큐에 있던 것 실행
        score, call_t, work_t = heapq.heappop(q2)
        waiting_time[score] += next_start - call_t # 대기시간 갱신
        next_start += work_t # 다음 시작 시간 갱신
        
        # 호출시간이 다음시작시간보다 작거나 같은 것들을 작업큐에 넣기
        while q1 and q1[0][0] <= next_start:
            c, s, w = q1.popleft()
            heapq.heappush(q2, (s, c, w))

    answer = [next_start] + waiting_time[1:]
    return answer

