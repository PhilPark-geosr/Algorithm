import sys
sys.stdin = open('input_14981.txt', 'r')
# input = sys.stdin.readline


# -------------- functionality -------------------#
def solution(A1, A2, A3, A4, orderlist):
    def check(num, A1, A2, A3, A4, dir):
        result = [] #뭐 로테이션 시킬건지
        # result.append(num) #자기자신 추가
        
        if num == 1: #1을 회전시키면
            # 2회전하는지 안하는지 확인

            if A1[2] != A2[-2]:
                result.append((2, dir*(-1))) #2회전
                if A2[2] != A3[-2]:
                    result.append((3, dir))
                    if A3[2] != A4[-2]:
                        result.append((4, dir*(-1)))

            # 같으면 나머지는 다 회전 안함

        elif num == 2:
            
            if A2[2] != A3[-2]:
                result.append((3, dir*(-1)))
                if A3[2] != A4[-2]:
                    result.append((4, dir))
            if A1[2] != A2[-2]:
                result.append((1, dir*(-1)))

        elif num == 3:
            
            
            if A3[2] != A4[-2]:
                result.append((4, dir*(-1)))

            if A2[2] != A3[-2]:
                result.append((2, dir*(-1)))
                #2번이 회전했을때만
                if A1[2] != A2[-2]:
                    result.append((1, dir))

        else:
            if A3[2] != A4[-2]:
                result.append((3, dir*(-1)))
                if A2[2] != A3[-2]:
                    result.append((2, dir))
                    if A1[2] != A2[-2]:
                        result.append((1, dir*(-1)))
            
            
            
        # print('rotate후보', result)
        return result

    def rotate(rotate_list, base_num, direction, A1, A2, A3, A4):

        def sub_rotate(arr, dir):
            if dir == 1:
                arr = [arr[7], arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6]]

            else:
                arr = [arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[0]]

            return arr
        
        if direction == 1: #시계방향

            # 자기자신 회전
            if base_num ==1:
                A1 = [A1[7], A1[0], A1[1], A1[2], A1[3], A1[4], A1[5], A1[6]]
            
            elif base_num == 2:
                A2 = [A2[7], A2[0], A2[1], A2[2], A2[3], A2[4], A2[5], A2[6]]

            elif base_num ==3:
                A3 = [A3[7], A3[0], A3[1], A3[2], A3[3], A3[4], A3[5], A3[6]]
            
            else:
                A4 = [A4[7], A4[0], A4[1], A4[2], A4[3], A4[4], A4[5], A4[6]]

           
            for num, dir in rotate_list:
                if num ==1:
                    A1 = sub_rotate(A1, dir)
                elif num ==2:

                    A2 = sub_rotate(A2, dir)
                elif num ==3:
                    A3 = sub_rotate(A3, dir)

                else:
                    A4 = sub_rotate(A4, dir)

              

                
        else: # 반시계

            if base_num == 1:
                    A1 = [A1[1], A1[2], A1[3], A1[4], A1[5], A1[6], A1[7], A1[0]]
                
            elif base_num ==2:
                A2 = [A2[1], A2[2], A2[3], A2[4], A2[5], A2[6], A2[7], A2[0]]
            
            elif base_num ==3:
                A3 = [A3[1], A3[2], A3[3], A3[4], A3[5], A3[6], A3[7], A3[0]]
            
            else: #base_num == 4
                A4 = [A4[1], A4[2], A4[3], A4[4], A4[5], A4[6], A4[7], A4[0]]

            for num, dir in rotate_list:
                if num ==1:
                    A1 = sub_rotate(A1, dir)
                elif num ==2:

                    A2 = sub_rotate(A2, dir)
                elif num ==3:
                    A3 = sub_rotate(A3, dir)

                else:
                    A4 = sub_rotate(A4, dir)

                
        
        return A1, A2, A3, A4
    def cal_score(arr1, arr2, arr3, arr4):
        score = 0
        if arr1[0] == 1: #S극
            score += 1
        if arr2[0] == 1:
            score +=2
        if arr3[0] == 1:
            score +=4
        if arr4[0] == 1:
            score += 8
        return score
    
    for num, direction in orderlist:
        rotate_list = check(num, A1, A2, A3, A4, direction)
        # print("direction",direction)
        A1, A2, A3, A4 = rotate(rotate_list, num, direction, A1, A2, A3, A4)

        # print(A1, A2, A3, A4)
    answer = cal_score(A1, A2, A3, A4)
    return answer
# ----------------- main -------------------------#

A1_string = input()
A1 = []
for elem in A1_string:
    A1.append(int(elem))

A2_string = input()
A2 = []
for elem in A2_string:
    A2.append(int(elem))

A3_string = input()
A3 = []
for elem in A3_string:
    A3.append(int(elem))
    
A4_string = input()
A4 = []
for elem in A4_string:
    A4.append(int(elem))

#print(A1, A2, A3, A4)
K = int(input())
# 결과
orderlist = []
for _ in range(K):
    num, direction = map(int, input().split())
    orderlist.append((num, direction))

#print(orderlist)
print(solution(A1, A2, A3, A4, orderlist))
