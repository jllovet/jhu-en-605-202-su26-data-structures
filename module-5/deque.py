# A deque (pronounced deck) is an ordered set of items from which items may be deleted at either end and into which items may be inserted at either end. Call the two ends left and right. This is an access-restricted structure since no insertions or deletions can happen other than at the ends. Implement the deque as a doubly-linked list (not circular, no header). Write InsertLeft and DeleteRight.

# type: ignore

class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class Deque:
    def __init__(self):
        self.left = None
        self.right = None

    def __str__(self):
        currentNode = self.left
        node_str = []
        while True:
            if currentNode is None:
                break
            else:
                node_str.append(
                    f"currentNode.data: {currentNode.data}, currentNode.next: {currentNode.next}, currentNode.previous: {currentNode.previous}")
                currentNode = currentNode.next
        return "\n".join(node_str)


def InsertLeft(d: Deque, data):
    node = Node(data)
    if d.left is None:
        d.left = node
        d.right = node
    else:
        node.next = d.left
        d.left.previous = node
        d.left = node
    return d


def DeleteRight(d: Deque):
    if d.right is None:
        return d
    if d.right.previous is None:
        d.right = None
        d.left = None
        return d
    if d.right.previous is not None:
        currentRight = d.right
        d.right.previous.next = None
        d.right = currentRight.previous
        return d


def main():
    d = Deque()
    InsertLeft(d, 1)
    InsertLeft(d, 2)
    InsertLeft(d, 3)
    print(d)
    print("now deleting...")
    DeleteRight(d)
    print(d)
    print("now deleting...")
    DeleteRight(d)
    print(d)


if __name__ == "__main__":
    main()
