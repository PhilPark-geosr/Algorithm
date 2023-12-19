import sys
# sys.stdin = open('input_14499.txt', 'r')
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())

grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)
order_list = list(map(int, input().split()))

direction = {
    1 : "동",
    2 : "서",
    3 : "북",
    4 : "남"
}


dice = {
    "a": 0,
    "b" : 0,
    "c" : 0,
    "d" : 0,
    "l" : 0,
    "r" : 0, 
}
# print('초기 dice', dice)

def move_dice(order, num):
    # print(direction[order] )
    old_dice = dice.copy()
    if direction[order] == "남":
        dice["a"], dice["b"], dice["c"], dice["d"] =dice["d"], dice["a"], dice["b"], dice["c"]
        # dice["a"] = old_dice["d"]
        # dice["b"] = old_dice["a"]
        # dice["c"] = old_dice["b"]
        # dice["d"] = old_dice["c"]

        
      


    elif direction[order] == "북":
        dice["a"], dice["b"], dice["c"], dice["d"] =dice["b"], dice["c"], dice["d"], dice["a"]
        # dice["a"] = old_dice["b"]
        # dice["b"] = old_dice["c"]
        # dice["c"] = old_dice["d"]
        # dice["d"] = old_dice["a"]
        

    elif direction[order] == "동": 
        dice["b"], dice["d"], dice["l"], dice["r"] =dice["l"], dice["r"], dice["d"], dice["b"]
        # dice["b"] = old_dice["l"]
        # dice["d"] = old_dice["r"]
        # dice["l"] = old_dice["d"]
        # dice["r"] = old_dice["b"]
        
    
    else:
        dice["b"], dice["d"], dice["l"], dice["r"] =dice["r"], dice["l"], dice["b"], dice["d"]
        # dice["b"] = old_dice["r"]
        # dice["d"] = old_dice["l"]
        # dice["l"] = old_dice["b"]
        # dice["r"] = old_dice["d"]
 
        
#test
# move_dice(3)
# print(dice)
dir = [(0,0), (0,1), (0,-1), (-1,0), (1,0)]
for order in order_list:
    # print("x, y", x,y, dice)
    dx, dy = dir[order]
    new_x, new_y = x + dx, y + dy
    
    if 0<=new_x<N and 0<=new_y<M: #안에 있을때만 이동
        cur_num = grid[new_x][new_y]
        move_dice(order, cur_num)
        # print("cur_num, target", cur_num, target)
        if cur_num !=0:
            dice['d'] = cur_num
            grid[new_x][new_y] = 0
        else:
            grid[new_x][new_y] = dice['d']
           
        
        # 맨 위 출력
        # print("주사위 맨위", dice, dice["d"])
        x, y = new_x, new_y
        # print(cur_num)
        print(dice["b"])
    else:
        # print('안움직입니다', x,y)
        continue



