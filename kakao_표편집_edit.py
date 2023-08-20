class Node:
    def __init__(self, value, next=None, prev=None):
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
            self.tail.prev = current

    def remove(self):
        self.removed.append(self.head)
        
        if self.head.prev is None:
            current = self.head
            next = current.next
            if next is not None:
                next.prev = None
        else:
            current = self.head.prev
            if current.next is not None and current.next.next is not None:
                next = current.next.next
                current.next = next
                next.prev = current
            else:
                current.next = None

        if self.head.next is None:
            self.head = current
        else:
            self.head = next

    def move_down(self, cnt):
        current = self.head
        for _ in range(cnt):
            if current.next is None:
                break
            current = current.next
        self.head = current

    def move_up(self, cnt):
        current = self.head
        for _ in range(cnt):
            if current.prev is None:
                break
            current = current.prev
        self.head = current

    def recover(self):
        node = self.removed.pop()
        if node.prev is not None:
            prev = node.prev
            prev.next = node
        
        if node.next is not None:
            next = node.next
            next.prev = node

def solution(n, k, cmd):
    ll = LinkedList()
    for i in range(n):
        ll.append(i)

    current = ll.head
    for _ in range(k):
        current = current.next
    ll.head = current

    for c in cmd:
        if c == "C":
            ll.remove()
        elif c == "Z":
            ll.recover()
        else:
            category, cnt = c.split(" ")
            if category == "U":
                ll.move_up(int(cnt))
            else:
                ll.move_down(int(cnt))

    ch = ["O"] * n

    for elem in ll.removed:
        idx = elem.value
        ch[idx] = "X"

    answer = "".join(ch)
    return answer
