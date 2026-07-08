class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"{self.data}, {self.left}, {self.right}"

def fibonacciTree(n, indent=" "): #type: ignore
    if n == 0:
        print(indent, "returning node")
        print(indent, 0)
        return Tree(0)
    if n == 1:
        print(indent, "returning node")
        print(indent, 1)
        return Tree(1)
    
    print(indent, f"Tree({n}, left=Tree({n-1}), right=Tree({n-2}))")
    return Tree(n, left=fibonacciTree(n-1, indent=indent+n*" "), right=fibonacciTree(n-2, indent=indent+n*" "))
    

if __name__ == "__main__":
    fibonacciTree(5)