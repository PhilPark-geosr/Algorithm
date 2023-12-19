N = 5
board = [[0] * (N+1) for _ in range(N+1)]
board2 = [[0] * (N+1) for _ in range(N+1)]
dirs = [(-1,0), (0,1), (1,0), (0,-1)]
def is_range(x,y):
    if 1<=x<=N and 1<=y<=N:
        return True
    else:
        return False


forward_dic = dict() #다음 방향 좌표 알려주는
def init_grid():
    x,y = int((N+1 )// 2), int((N+1) // 2)  # 배열의 중앙 좌표
    # print('초기', x,y)
    d = 0
    dist = 1
    #초기세팅
    forward_dic[0] = (x,y,d)
    value = 1
    while True:
        # 두번씩 움직인다
        for _ in range(2):
            # 거리만큼 간다
            for _ in range(dist):
                new_x, new_y = x + dirs[d][0], y+ dirs[d][1] #이동
                # print(new_x, new_y)
                if is_range(new_x, new_y) == False: #밖 벗어나면 종료
                    return
                # 아니면 기록
                board[new_x][new_y] = value
                forward_dic[value] = (new_x, new_y, d) #기록
                value +=1
                x,y = new_x, new_y
            # 끝까지 갔으면 방향 전환
            d = (d+1)%4
            forward_dic[value-1] = (new_x, new_y, d)  # 기록
        # 다 갔으면 거리 증가
        dist +=1
reverse_dic = dict()
def init_revsere_grid():
    x,y = 1,1  # 배열의 중앙 좌표
    # print('초기', x,y)
    d = 2
    dist = N-1
    #초기세팅
    reverse_dic[0] = (x,y,d)
    value = 1
    while True:
        if dist ==-1:
            return
        # 두번씩 움직인다
        if dist == N-1:
            for _ in range(3):
                # 거리만큼 간다
                for _ in range(dist):
                    new_x, new_y = x + dirs[d][0], y+ dirs[d][1] #이동
                    print(new_x, new_y)
                    # 아니면 기록
                    board2[new_x][new_y] = value
                    reverse_dic[value] = (new_x, new_y, d) #기록
                    value +=1
                    x,y = new_x, new_y
                # 끝까지 갔으면 방향 전환
                d = d-1 if d>0 else 3
                reverse_dic[value-1] = (new_x, new_y, d)  # 기록
        else:
            for _ in range(2):
                # 거리만큼 간다
                for _ in range(dist):
                    new_x, new_y = x + dirs[d][0], y+ dirs[d][1] #이동
                    print(new_x, new_y)
                    # 아니면 기록
                    board2[new_x][new_y] = value
                    reverse_dic[value] = (new_x, new_y, d) #기록
                    value +=1
                    x,y = new_x, new_y
                # 끝까지 갔으면 방향 전환
                d = d-1 if d>0 else 3
                reverse_dic[value-1] = (new_x, new_y, d)  # 기록
        # 다 갔으면 거리 증가
        dist -=1
init_grid()
# print(board)
# print(forward_dic)
init_revsere_grid()
print(board2)
print(reverse_dic)