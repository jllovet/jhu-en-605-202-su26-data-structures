import lab2.convert.errors as errors
import lab2.internal.parse.validate as validate
from typing import Optional


class Node:
    def __init__(self, parent, data, left=None, right=None):
        self.parent: Node | None = parent
        self.data: str = data
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def __str__(self, level=1):
        return f"{self.data}\n{'\t'*level}left: {self.left}\n{'\t'*level}right: {self.right}"

    def __iter__(self):
        if self.left:
            yield from self.left
        if self.right:
            yield from self.right
        yield self.data
