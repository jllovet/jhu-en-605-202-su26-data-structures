class Stack:
    def __init__(self, max_height: int = -1):
        self.max_height = max_height
        self.data = []
        self.height = len(self.data)

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def is_full(self) -> bool:
        return False

    def peek(self) -> str:
        return ""
    
    def pop(self) -> str:
        return self.data.pop()

    def push(self, item: str) -> bool:
        if self.height == self.max_height:
            return False
        self.data.append(item)
        self.height += 1
        return True
