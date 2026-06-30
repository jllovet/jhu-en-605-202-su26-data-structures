# Implement a deque from problem 1 as a doubly-linked circular list with a header. Write InsertRight and DeleteLeft.

# type: ignore

class Node:
    def __init__(self, data, isHeader=False):
        self.isHeader = isHeader
        self.data = data
        self.previous = None
        self.next = None
    
    def __str__(self) -> str:
        if self.isHeader:
            return str(f"(header) {self.data}")
        return str(self.data)


class Deque:
    def __init__(self):
        self.header = Node(0, isHeader=True)
        self.header.next = self.header
        self.header.previous = self.header
        self.left = self.header
        self.right = self.header

    def __str__(self):
        node_str = [f"length of data: {self.header.data}", f"left: {self.left}", f"right: {self.right}"]
        currentNode = self.header
        node_str.append(f"isHeader: {currentNode.isHeader}, data: {currentNode.data}, next: {currentNode.next}, previous: {currentNode.previous}")
        currentNode = currentNode.next
        for i in range(self.header.data):
            node_str.append(
                f"isHeader: {currentNode.isHeader}, data: {currentNode.data}, next: {currentNode.next}, previous: {currentNode.previous}")
            currentNode = currentNode.next
        return "\n".join(node_str)



def InsertRight(d: Deque, data):
    node = Node(data, isHeader=False)
    if d.header.data == 0:
        node.previous = d.header
        node.next = d.header
        d.left = node
        d.right = node
        d.header.next = node
        d.header.previous = node
    else:
        node.previous = d.right
        d.right.next = node
        node.next = d.header
        d.header.previous = node
        d.right = node
    d.header.data += 1
    return d


def DeleteLeft(d: Deque):
    # Case 0
    if d.header.data == 0:
        return d
    # Case 1
    if d.left.next.isHeader:
        d.left = d.header
        d.right = d.header
        d.header.next = d.header
        d.header.previous = d.header
    # Case > 1
    if not d.left.next.isHeader:
        d.left.next.previous = d.header
        d.header.next = d.left.next
        d.left = d.left.next
    d.header.data -= 1
    return d


def main():
    d = Deque()
    print(d.header.next)
    print("populating...")
    InsertRight(d, 1)
    print(d)
    print()
    InsertRight(d, 2)
    print(d)
    print()
    InsertRight(d, 3)
    print(d)
    print()
    print("now deleting...")
    DeleteLeft(d)
    print(d)
    print()
    print("now deleting...")
    DeleteLeft(d)
    print(d)
    print()
    print("now deleting...")
    DeleteLeft(d)
    print(d)
    print()
    print("now deleting...")
    DeleteLeft(d)
    print(d)
    print()


if __name__ == "__main__":
    main()
