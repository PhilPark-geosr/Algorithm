class Node:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.removed = []
 
    def append(self, value):
        new_node = Node(value)
        current = self.tail 
        # 아무것도 없을 경우 
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else: # 무언가 있을경우
            self.tail.next = new_node
            self.tail = self.tail.next
            self.tail.prev = current 

    def remove(self):
        # print(f"{self.head.value}를 제거하겠습니다")
        # 제거된 항목 저장
        self.removed.append(self.head)
        
        if self.head.prev == None:
            current = self.head
            next = current.next

            # 하나만 있을때 지우는 경우!!    
            if next is not None:
                next.prev = None
            


        else: #맨 앞에 걸 지우는 경우가 아닌 경우 
            current = self.head.prev #한칸 전으로 이동
        
        
            if current.next.next !=None:
                next = current.next.next
                current.next = next
                next.prev = current
            else:
                current.next =None
            

        #prev
        # if next != None:
        #     next.prev = current

        # head 이동
        if self.head.next == None: #맨 끝에걸 지우는 경우
            self.head = current #바로 윗행 선택
        else: #맨끝을 지우는 경우가 아닌경우
            self.head = next

    # 아래로 이동
    def move_down(self, cnt):
        current = self.head
        for _ in range(cnt):
            if current.next == None:
                break
            current = current.next
        self.head = current
    # 위로 이동
    def move_up(self, cnt):
        current = self.head
        for _ in range(cnt):
            if current.prev == None:
                break
            current = current.prev
        self.head = current

    def recover(self):
        # 가장최근꺼 꺼냄
        node = self.removed.pop()
        # print(f"node, value, prev, next, {node.value, node.prev.value, node.next.value}")
        # 연결관계 회복
        if node.prev is not None:
            prev = node.prev
            prev.next = node
        
        if node.next !=None:
            next = node.next
            next.prev = node
        
        
def solution(n, k, cmd):
    # Linked List 만들기
    ll = LinkedList()
    for i in range(n):
        ll.append(i)

    # 확인
    # current = ll.head
    # for _ in range(n):
    #     print(current.value)
    #     current= current.next

    # k만큼 커서 이동
    current = ll.head
    for _ in range(k):
        current = current.next
    ll.head = current
    # print(ll.head.prev.value)

    # test
    # ll.move_down(2)
    
    # ll.remove()
    # print(ll.head.value)
    # # print(ll.removed[0].prev.value)
    # ll.recover()
    # print(ll.head.value, ll.head.prev.value, ll.head.next.value)


    for c in cmd: #행동 시작
        # print(ll.head.value)
        if c =="C":
            ll.remove()
        elif c == "Z":
            ll.recover()
        else:
            category, cnt = c.split(" ")
            if category == "U":
                ll.move_up(int(cnt))
            else:
                ll.move_down(int(cnt))

    ch = ["O"]*n

    for elem in ll.removed:
        # print("elem.value",elem.value)
        idx = elem.value
        ch[idx] = "X"
    # print(ch)
    #결과 추출
    answer = "".join(ch)
    return answer

    # print('removed_list', ll.removed)
                 
