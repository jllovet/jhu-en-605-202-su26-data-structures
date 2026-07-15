import lab2.convert.errors as errors
import lab2.internal.parse.validate as validate
from typing import Optional


class Node:
    """Implementation of the tree ADT"""

    def __init__(self, parent=None, data="", left=None, right=None):
        """Initializes a node with the parent optionally specified

        Args:
            parent: int specifying maximum height of stack. If max_height
            is a nonnegative integer, then max_height is the maximum height
            for the stack. If max_height < 0, then the stack is unbounded.

        Returns:
            Stack initialized with empty data and maximum height set to max_height

        Raises:
            None

        Side Effects:
            None

        Idempotent:
            True
        """
        self.parent: Optional[Node] = parent
        self.data: str = data
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def __str__(self, level: int = 1) -> str:
        """Returns a str representation of the tree for printing
        TODO: Have the indentation print in a proper tree structure
        Args:
            level: int specifying indentation of children

        Returns:
            str representation of the tree

        Raises:
            None

        Side Effects:
            None

        Idempotent:
            True
        """
        return f"{self.data}\n{'\t'*level}left: {self.left}\n{'\t'*level}right: {self.right}"

    def __iter__(self):
        """Yield the nodes of the tree in post-order

        Inspired by the strategy described here: https://martinheinz.dev/blog/88
        
        Args:
            None

        Returns:
            Yields the elements of the tree in post-order.

        Raises:
            None

        Side Effects:
            None

        Idempotent:
            False
        """
        if self.left:
            yield from self.left
        if self.right:
            yield from self.right
        yield self.data
