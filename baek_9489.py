import sys
import collections
sys.stdin = open('input_9489.txt', 'r')

while True:
    n, k = map(int, input().split())
    if (n, k) == (0,0):
        break
    nodelist = list(map(int, input().split()))
    # print(n, k , nodelist)
    prev = nodelist[0]
    stack = [prev]
    result = []
    for elem in nodelist[1:]:
        # print(elem, stack)
        if elem-prev >1:
            result.append(stack)
            stack = []
            stack.append(elem)
        else:
            stack.append(elem)
        prev = elem
    if stack:
        result.append(stack)

    # print(result)

    dic = collections.defaultdict(list)


    q = collections.deque()
    q.append(nodelist[0])
    parent = collections.defaultdict(int)
    for elem in result[1:]:
        while q:
            current = q.popleft()
            if len(dic[current]) == 0:
                dic[current] = elem
                for x in elem:
                    parent[x] = current
                    q.append(x)
                break

    # print(dic)
    # print(parent)
    my_parent = parent[k]
    count =0
    for node in nodelist[1:]:
        # print(node)
        if parent[node] != my_parent and parent[parent[node]] == parent[my_parent]:
            count+=1
    print(count)



