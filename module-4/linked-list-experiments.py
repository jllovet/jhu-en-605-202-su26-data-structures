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


q = LinkedList()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)
reverse(q)
traverse(q)