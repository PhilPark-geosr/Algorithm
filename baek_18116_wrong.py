import sys
import collections
sys.stdin = open('input_18116.txt', 'r')
input = sys.stdin.readline

robot = collections.defaultdict(list)
part = dict()

N = int(input())
cnt = 10**6 +1
for _ in range(N):
    Q = input().split()
    # print("Q", Q)
    if Q[0] == 'I':
        a, b = int(Q[1]), int(Q[2])
        if a not in part and b not in part: #등록이 안되어 있을때
            part[a] = cnt
            part[b] = cnt
            robot[cnt].append(a)
            robot[cnt].append(b)
            cnt+=1
        elif a in part and b not in part:
            num = part[a] #로봇번호 추출
            part[b] = num #등록
            robot[num].append(b) #로봇에 추가

        elif a not in part and b in part:
            num = part[b]
            part[a] = num
            robot[num].append(a)

        else:
            pass

    else: #Q[0] == "Q"
        a = int(Q[1])
        if a not in part: #어떤 로봇의 부품인지 모를때는
            # part[a] = i #등록
            # robot[i].append(a)
            print(1)
        else:

            num = part[a]
            print(len(robot[num]))

print(robot)
print(part)