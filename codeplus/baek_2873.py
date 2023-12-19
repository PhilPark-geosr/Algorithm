import sys
sys.stdin = open('input_2873.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())

grid = [[0]*(M+1)]
for _ in range(N):
    line = list(map(int, input().split()))
    line.insert(0,0)
    grid.append(line)
# print('grid', grid)

if N%2 ==0 and M%2 ==1: # 행 짝수, 열 홀수 --> 다 거치는게 베스트
    iter_string = "D"*(N-1)+"R" + "U"*(N-1) + "R"
    answer= iter_string*(M//2) + "D"*(N-1)
    print(answer)

elif N%2 ==1 and M%2 ==0: #행 홀수 열 짝수
    iter_string = "R"*(M-1)+"D" + "L"*(M-1) + "D"
    answer= iter_string*(N//2) + "R"*(M-1)
    print(answer)

elif N%2 ==1 and M%2 ==1:  #둘다 홀수
    iter_string = "R"*(M-1)+"D" + "L"*(M-1) + "D"
    answer= iter_string*(N//2) + "R"*(M-1)
    print(answer)

else:
    # 최솟값 위치 찾기
    min_value = float('inf')
    min_x, min_y = None, None
    for i in range(1, N+1):
        for j in range(1, (M)//2+1):
            if i %2 ==0: #작수일때
                if grid[i][2*j -1] < min_value:
                    min_value = grid[i][2*j -1]
                    min_x, min_y = i, 2*j-1
                
            else:
                if grid[i][2*j] < min_value:
                    min_value = grid[i][2*j]
                    min_x, min_y = i, 2*j       
    # print('min_value, min_x, min_y', min_value, min_x, min_y)
    r, c = min_x, min_y

    # r,c이전까지 이동
    way = ""
    # free_lenght = r-1 # R-->D -->L 하는 길이

    
    if r %2 ==1: #최솟값 행의 값이 홀수
        iter_string = "R"*(M-1)+"D" + "L"*(M-1) + "D"
        way+= (r-1)//2*iter_string + "D"

        # 블랭크가 있는 칸에서의 이동
        prev = "RD"
        x, y = r+1, 1
        while y <M:
            # print('x,y',x,y, way)
            if prev =="RD":
                new_x, new_y = r, y+1
                if (new_x, new_y) == (r, c): #블랭크에 도착하면

                    way+="R"
                    prev = "RD"
                    x,y = r+1, y+1
                else:

                    way+="RU"
                    prev ="RU"
                    x, y = new_x, new_y

            else: #prev =="RU"
                new_x, new_y = r+1, y+1
                way += "RD"
                prev ="RD"
                x, y = new_x, new_y
        

        # print('중간값', way)
        #이제 나머지 길이만큼 다시 프리하게
        iter_string = "D" + "L"*(M-1)+"D" + "R"*(M-1)
        way +=(N-r-1)//2*iter_string 
        print(way)

    else: # 최솟값 행의 값이 짝수
        iter_string = "R"*(M-1)+"D" + "L"*(M-1) + "D"
        way+= (r-1)//2*iter_string 
        way+="D"
        # 블랭크가 있는 칸에서의 이동
        prev = "RD"
        x, y = r, 1
        while y <M:

            if prev =="RD":
                new_x, new_y = r-1, y+1
                way+="RU"
                prev ="RU"
                x, y = new_x, new_y
            else: #prev =="RU"
                new_x, new_y = r, y+1
        
                if (new_x, new_y) == (r, c): #블랭크에 도착하면
                    way+="R"
                    prev = "RU"
                    x,y = r-1, y+1
                else:
                    way+="RD"
                    prev ="RD"
                    x, y = new_x, new_y
        

        iter_string = "D" + "L"*(M-1)+"D" + "R"*(M-1)
        way +=(N-r)//2*iter_string 
        print(way)

        