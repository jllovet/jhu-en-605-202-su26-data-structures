from typing import List
type Algorithm = str


class Context:
    def __init__(self, algorithm: Algorithm, xs: List):
        self.algorithm: Algorithm = algorithm
        self.comparisons: int = 0
        self.list_size: int = len(xs)
        self.xs: List[int] = xs

    def __repr__(self):
        return str(self.__dict__)
