
# 시간초과 풀이
def solution(food_times, k):
    import collections
    q = collections.deque()
    # make q:
    for i, value in enumerate(food_times):
        q.append((value, i+1))
    # print(q)

    time =0

 
    while q:
        
        # print(q, time)
    
        value, idx = q.popleft()
        if time >=k:
            return idx
        

        new_value = value-1
        if new_value !=0:
            q.append((new_value, idx))
        time+=1

    # print(time)



    return -1

# 정답 풀이
def solution(food_times, k):
    import heapq
    q =[]
    # make heapq:
    for i, value in enumerate(food_times):
        heapq.heappush(q, (value, i+1))
        # q.append((value, i+1))
    # print(q)

    time =0

    len_food = len(q)
    previous= 0 #전에 다 먹어치운 값
    while q:
        value, idx = q[0] #가장 최소의 것을 찾자
        # print(value, idx, previous)
        # 일단 다 먹어본다
        time = (value-previous) * (len_food)
        # print(q, time)

        if time >k: # 시간이 넘어가면.. 남은 음식 중 
            answer_idx = (k) % len_food
            q.sort(key=lambda x : x[1])
            return q[answer_idx][1]
        
        else: #시간 안넘어갔을 경우, 다 먹어치운걸 제거하고, 상태를 업데이트 한다
            previous, _ = heapq.heappop(q) #직전에 먹어치운값 갱신 및 다 먹어치운 테이블 제거
            len_food -=1
            k -=time
    
    # 시간이 다 안지났는데 먹을 음식이 없는 경우
    return -1

food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))