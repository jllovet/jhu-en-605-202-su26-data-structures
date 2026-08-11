type Algorithm = str


class Context:
    def __init__(self, algorithm: Algorithm):
        self.algorithm: Algorithm = algorithm
        self.comparisons: int = 0
