def solution(k, room_number):
    import collections
    import heapq
    check_dic = dict()
    q = [] #차있는방 
    
    def find_room(number):
        # print('number, q', number, q)
        if number not in check_dic: # 아직 배정 안되었으면
            check_dic[number] = True #방이 차있음을 
            heapq.heappush(q, number+1) #바로 오른쪽 번호 넣어놓기
            return number
        if number in check_dic: # 배정되어있는 경우면
            temp = []
            while q :
                if q[0] <= number:
                    # 일단 뺴놓기
                    elem = heapq.heappop(q)
                    temp.append(elem)
                else: # q[0] > number
                    if q[0] not in check_dic:
                        elem = heapq.heappop(q)
                        check_dic[elem] = True
                        heapq.heappush(q,elem+1)
                        # 다시 채워주기
                        
                        while temp:
                            elem2 = temp.pop()
                            if elem2 not in check_dic:
                                heapq.heappush(q, elem2)   
                        return elem
                    else:
                        heapq.heappop(q)

    answer = []
    for elem in room_number:
        # print('elem', elem,'q', q, 'check_dic', check_dic, answer)
        my_num = find_room(elem)
        
        answer.append(my_num)
        # print('elem', elem,'q', q, 'check_dic', check_dic, answer)
    
    
    return answer