import sys
sys.stdin = open('input_1343.txt', 'r')

board = input()
# . 갯수찾기


    


boardlist = board.split('.')
print(boardlist)

# flag = True #가능여부
# result = ""
# for case in boardlist: #해봤자 n개 50개미만
#     if case == "":
#         continue
#     if len(case)%2 !=0:
#         flag = False
#         break
#     num_a = len(case)//4
#     num_b = (len(case) - num_a)//2
#     result += 'A'*num_a + 'B'*num_b
temp =""
flag =True
result = ""
for elem in board:
    print(elem, temp)
    if elem !=".":
        temp +=elem
    else: #elem =='.'
        
        if len(temp) ==0:
            result+="."
        else:
            
            if len(temp)%2 !=0:
                flag = False
                break
            num_a = len(temp)//4
            num_b = (len(temp) - num_a)//2
            result += 'AAAA'*num_a + 'BB'*num_b +"."
            print(result)
            temp =""
print(result)
# board = "BB.AAAAAAAABB..AAAAAAAA...AAAABB"



if flag ==False:
    print(-1)
else:
    pass