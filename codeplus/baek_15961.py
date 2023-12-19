import sys
#sys.stdin = open('input_15961.txt', 'r')
input = sys.stdin.readline

N, d, K, c = map(int, input().split())
numbers = []
for _ in range(N):
    elem =int(input())
    numbers.append(elem)

numbers.extend(numbers) #두배 확장
# print("numbers", numbers)

dish = dict() #먹은 접시 기록
l = 0
r = K-1

for i in range(l, r+1):
    if numbers[i] in dish:
        dish[numbers[i]] +=1
    else:
        dish[numbers[i]] = 1
# print('초기 dish', dish)

answer = 0
while l < N:
    # print(dish)
    if c in dish:
        cnt = len(dish) # 원래 있던거라 가짓수 추가 안됨
    else:
        cnt = len(dish) +1 # 추가로 한접시 추가

    # 최댓값 갱신
    if cnt > answer:
        answer = cnt

    # 포인터 이동
    # 좌측 이동
    dish[numbers[l]] -=1
    if dish[numbers[l]] ==0:
        dish.pop(numbers[l], None)
    l+=1
    # 우측 이동
    r+=1
    if numbers[r] in dish:
        dish[numbers[r]]+=1
    else:
        dish[numbers[r]] =1

print(answer)