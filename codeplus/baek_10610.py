import sys
sys.stdin= open('input_10610.txt', 'r')

inputlist = input()
numbers = []
for elem in inputlist:
    numbers.append(int(elem))

# print(numbers)
def solution(numbers):
    answer = -1
    if 0 not in numbers or sum(numbers)%3 !=0:
        return answer
    numbers.sort(reverse = True)
    numbers = list(map(str, numbers))
    answer = "".join(numbers)
    
    return answer



print(solution(numbers))