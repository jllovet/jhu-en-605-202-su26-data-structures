class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        return f"{self.data}"

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
            self.tail = n
        elif self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = n # type: ignore
            self.tail = n
        self.length += 1


def traverse(seq: LinkedList):
    # print("traverse:", seq)
    list_traverse(seq.head)

def list_traverse(n: Node | None):
    # print("list_traverse:", n)
    if n is not None:
        print(n)
        # print("calling list_traverse:", n.next)
        list_traverse(n.next)


def reverse(seq: LinkedList):
    # handle empty list first
    if seq.head is None:
        return seq
    # initialize previous node to head
    previous = seq.head
    # handle single-element list (no reversal required)
    if previous.next is None:
        return seq
    # start incrementing
    current = previous.next
    # reverse pointer for special case of head
    previous.next = None
    while current.next is not None:
        next = current.next # store next node
        current.next = previous # reverse pointer
        previous = current # increment forward
        current = next # increment forward
    
    seq.head = current # set head to last node
    current.next = previous # reverse pointer
    return seq # all done!


def swap(seq: LinkedList, m, n: int):
    # degenerate cases
    if seq.head is None:
        return
    if seq.head.next is None:
        return
    if m > (seq.length - 1):
        return # Error or Exception
    if n > (seq.length - 1):
        return # Error or Exception
    # legitimate cases
    if m == n:
        return # no operation
    # use aliases to reduce to a simple case
    if m > n:
        a = n
        b = m
    elif n > m:
        a = m
        b = n
    # b > a
    a_current = seq.head
    b_current = seq.head
    a_pos = 0
    b_pos = 0
    a_previous = a_current
    b_previous = b_current
    while (b_previous.next is not None) and (b_pos < b): #type:ignore
        if a_pos < a: # we know that a_current.next is not None
            a_previous = a_current
            a_current = a_current.next #type:ignore
            a_pos += 1
        b_previous = b_current
        b_pos += 1
        b_current = b_current.next #type:ignore
    if a == 0:
        tmp = b_current.next #type:ignore
        b_current.next = a_current.next #type:ignore
        b_previous.next = a_current #type:ignore
        a_current.next = tmp #type:ignore
    if a > 0:
        tmp = b_current.next #type:ignore
        b_current.next = a_current.next #type:ignore
        b_previous.next = a_current #type:ignore
        a_previous.next = b_current #type:ignore
        a_current.next = tmp #type:ignore


q = LinkedList()
q.append(0)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)
# reverse(q)
# traverse(q)

swap(q,5,4)
traverse(q)
