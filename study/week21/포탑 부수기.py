import sys
import collections
sys.stdin = open('input_포탑부수기.txt', 'r')
input = sys.stdin.readline
N, M , K = map(int, input().split())

grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)

print("grid", grid)

# 공격받은 시점 기록
attacked = [[0]*M for _ in range(N)]


def count_port(grid):
    count =0
    for i in range(N):
        for j in range(M):
            if grid[i][j] !=0:
                count+=1
    if count ==1: #포탑 하나만 남았으면..
        return False
    return True


def find_attacker(time):
    #최솟값 찾기
    min_value = 5001 #최대 공격력
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                continue
            if grid[i][j] < min_value:
                min_value = grid[i][j]
    print("min_value",min_value)
    # 최솟값 리스트들 정리
    candidates = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == min_value:
                candidates.append((attacked[i][j], i+j, j))
    candidates.sort(key =lambda x: (-x[0], -x[1], -x[2]))
    print("candidates", candidates)

    target = candidates[0]
    # 공격 포탑선정
    target_i, target_j = target[1] - target[2], target[2]
    print("target_i, target_j", target_i, target_j)

    #공격력 증가
    grid[target_i][target_j] += N+M

    # 공격시간 업데이트
    attacked[target_i][target_j] = time

    # 변화있었던 부분 체크
    ch[target_i][target_j] =1

    return target_i, target_j


def find_attacked(time, acttack_i, attack_j): #현재시간, 공격하는 포탑 좌표
    # 가장 높은 공격력 찾기

    max_value = 0
    for i in range(N):
        for j in range(M):
            if (i,j) == (acttack_i, attack_j):
                continue
            if grid[i][j] == 0:
                continue
            if grid[i][j] > max_value:
                max_value = grid[i][j]
    print("max_value",max_value)

    # 최댓값 리스트들 정리
    candidates = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == max_value:
                candidates.append((attacked[i][j], i+j, j))
    candidates.sort(key =lambda x: (x[0], x[1], x[2]))
    print("candidates", candidates)


    target = candidates[0]
    # 공격대상 포탑선정
    target_i, target_j = target[1] - target[2], target[2]
    print("target_i, target_j", target_i, target_j, grid[target_i][target_j])

    return target_i, target_j 

def attack(attack_i, attack_j, attacked_i, attacked_j):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0] #우 하 좌 상
    #레이저
    visited = [[0]*M for _ in range(N)] #방문기록
    q= collections.deque()
    q.append((0, attack_i, attack_j, []))
    visited[attack_i][attack_j]=1
    
    attack_value = grid[attack_i][attack_j] #공격력
    raser = False

    while q:
        distance, x, y , roads = q.popleft()
        print(x,y, roads)
        if (x,y) == (attacked_i, attacked_j):
            print("최단경로", distance, roads)

            raser = True #레이저 공격 완료

            #경로만큼 공격
            
            print('공격력', attack_value)
            for i, j in roads:
                if (i,j) == (attacked_i, attacked_j):
                    grid[i][j] -= attack_value
                else:
                    grid[i][j] -= attack_value//2
                # 공격한거 체크
                ch[i][j] =1


            break

        for k in range(4):
            new_x, new_y = x + dx[k], y + dy[k]

            # 좌표 처리
            if new_x <0 :
                new_x = N-1
            elif new_x > N-1:
                new_x = 0
            else:
                new_x = new_x

            if new_y <0 :
                new_y = M-1
            elif new_y > M-1:
                new_y = 0
            else:
                new_y = new_y
            
            if visited[new_x][new_y] == 0 and grid[new_x][new_y] !=0:
                # print("new_x, new_y",new_x, new_y, grid[new_x][new_y])
                visited[new_x][new_y] =1
                
                q.append((distance+1, new_x, new_y, roads + [(new_x, new_y)]))

            
    if raser ==False: # 레이저 공격 안될때만 포탑 공격
        print('포탑공격')
        dx = [0, 1, 0, -1, 1, 1, -1, -1]
        dy = [1, 0, -1, 0, 1, -1, 1, -1]

        # 공격 받는 위치 일단 감소
        grid[attacked_i][attacked_j] -= attack_value 
        
        # 공격한거 체크
        ch[attacked_i][attacked_j] =1

        for k in range(8):
            new_x, new_y = attacked_i + dx[k], attacked_j + dy[k]
             # 좌표 처리
            if new_x <0 :
                new_x = N-1
            elif new_x > N-1:
                new_x = 0
            else:
                new_x = new_x

            if new_y <0 :
                new_y = M-1
            elif new_y > M-1:
                new_y = 0
            else:
                new_y = new_y

            if grid[new_x][new_y] !=0 and (new_x, new_y) != (attack_i,attack_j): #공격자 아닌것들에 대해서만
                
                print("공격받는 대상", new_x, new_y)
                grid[new_x][new_y] -= attack_value//2
                # 공격 받는거 체크
                ch[new_x][new_y] =1
        
        
    return

for t in range(1, K+1):

    ch = [[0]*M for _ in range(M)]

    # 공격포탑
    attack_i, attack_j = find_attacker(t)
    # 공격대상
    attacked_i, attacked_j = find_attacked(t, attack_i, attack_j)
    # 공격
    attack(attack_i, attack_j, attacked_i, attacked_j)

    print("ch",ch)


    # 포탑 파괴
    for i in range(N):
        for j in range(M):
            if grid[i][j]<0:
                grid[i][j] =0

    #정비
    for i in range(N):
        for j in range(M):
            if ch[i][j] ==0 and grid[i][j]!=0:
                grid[i][j] +=1

    print("grid", grid)


#가장 강한 공격력 도출
answer = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            continue
        if grid[i][j] > answer:
            answer =grid[i][j]

print(answer)


