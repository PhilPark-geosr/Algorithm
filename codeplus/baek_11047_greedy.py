import sys
sys.stdin = open('input_11047.txt')
# input = sys.stdin.readline

N, K = map(int, input().split())
money_list = []
for _ in range(N):
    money = int(input())
    money_list.append(money)

#정렬
money_list.sort(reverse = True)
# print('money_list', money_list)

def cal_coin(target, money):
   
    cnt =0
    while True:
        if target - cnt*money >=0:
            cnt+=1
            
        else:
            cnt-=1
            break
    return target- cnt*money, cnt



target = K
answer = 0
for money in money_list:
    target, cnt = cal_coin(target, money)
    # print(money, target, cnt)
    answer +=cnt
    if target <=0:
        break

print(answer)
