from typing import Optional, List
from lab3.huffman.encoding.encode import EncodingData


class Node:
    """Implementation of the tree ADT"""

    def __init__(self, parent=None, data="", left=None, right=None):
        """Initializes a node with the parent optionally specified

        Args:
            parent: optional pointer back to parent Node

        Returns:
            Node with data and pointers to parent node and left, right children

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

    def __str__(self) -> str:
        """Returns a str representation of the tree for printing
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
        return f"[{self.data}]{self.left}{self.right}"

    def __iter__(self, order="preorder"):
        """Yield the nodes of the tree in preorder

        Inspired by the strategy described here: https://martinheinz.dev/blog/88

        Args:
            None

        Returns:
            Yields the elements of the tree in preorder.

        Raises:
            None

        Side Effects:
            None

        Idempotent:
            False
        """
        if order == "preorder":
            yield from self.preorder()
        if order == "postorder":
            yield from self.postorder()
        if order == "inorder":
            yield from self.inorder()

    def preorder_as_str(self):
        """Forces evaluation of preorder iteration and joins elements into string"""
        return "".join(self.preorder())

    def inorder_as_str(self):
        """Forces evaluation of inorder iteration and joins elements into string"""
        return "".join(self.inorder())

    def postorder_as_str(self):
        """Forces evaluation of postorder iteration and joins elements into string"""
        return "".join(self.postorder())

    def preorder(self):
        """Yield the nodes of the tree in preorder

        Inspired by the strategy described here: https://martinheinz.dev/blog/88

        Given the tree: ABCDEFG

        preorder yields the tree's elements as ABDECFG

        Args:
            None

        Returns:
            Yields the elements of the tree in preorder.

        Raises:
            None

        Side Effects:
            None

        Idempotent:
            False
        """
        yield self.data
        if self.left:
            yield from self.left.__iter__(order="preorder")
        if self.right:
            yield from self.right.__iter__(order="preorder")

    def postorder(self):
        """Yield the nodes of the tree in postorder

        Inspired by the strategy described here: https://martinheinz.dev/blog/88

        Given the tree: ABCDEFG

        postorder yields the tree's elements as: DEBFGCA

        Args:
            None

        Returns:
            Yields the elements of the tree in postorder.

        Raises:
            None

        Side Effects:
            None

        Idempotent:
            False
        """
        if self.left:
            yield from self.left.__iter__(order="postorder")
        if self.right:
            yield from self.right.__iter__(order="postorder")
        yield self.data

    def inorder(self):
        """Yield the nodes of the tree in order

        Inspired by the strategy described here: https://martinheinz.dev/blog/88

        Given the tree: ABCDEFG

        inorder yields the tree's elements as: DBEAFCG

        Args:
            None

        Returns:
            Yields the elements of the tree in order.

        Raises:
            None

        Side Effects:
            None

        Idempotent:
            False
        """
        if self.left:
            yield from self.left.__iter__(order="inorder")
        yield self.data
        if self.right:
            yield from self.right.__iter__(order="inorder")


class MinHeap:
    def __init__(self):
        self.data = []

    def __str__(self) -> str:
        return f"{self.data}"

    def length(self):
        return len(self.data)

    def parent_index(self, index: int) -> int:
        if index == 0:
            return 0
        reduction = 2 if index % 2 == 0 else 1
        parent = (index - reduction) // 2
        return parent

    def left_child_index(self, index: int) -> int | None:
        if index >= self.length():
            return None
        left_child_index = (index * 2) + 1
        return left_child_index

    def right_child_index(self, index: int) -> int | None:
        if index >= self.length():
            return None
        right_child_index = (index * 2) + 2
        return right_child_index

    def enqueue(self, item):
        # percolate up
        self.data.append(item)
        index = self.length() - 1
        while index > 0:
            parent_index = self.parent_index(index)
            if self.data[parent_index] > self.data[index]:
                tmp = self.data[parent_index]
                self.data[parent_index] = self.data[index]
                self.data[index] = tmp
            index = parent_index

    def dequeue(self):
        if not self.data:
            return None
        if self.length() == 1:
            return self.data.pop()
        last = self.data.pop()
        index = 0
        self.data[index] = last
        # percolate down
        while True:
            if index >= self.length() - 1:
                break
            current = self.data[index]
            lc_index = self.left_child_index(index)
            rc_index = self.right_child_index(index)
            left_child = None
            right_child = None
            size = self.length() - 1
            if lc_index:
                left_child = self.data[lc_index] if lc_index <= size else None
            if rc_index:
                right_child = self.data[rc_index] if rc_index <= size else None

            if left_child is not None and right_child is not None:
                max_child = max(left_child, right_child)  # type: ignore
            if right_child is None:
                max_child = left_child
            if left_child is None:
                break

            if max_child == left_child:
                max_child_index = lc_index
            else:
                max_child_index = rc_index
            if max_child < current:
                tmp = self.data[int(index)]
                self.data[index] = self.data[int(
                    max_child_index)]  # type: ignore
                self.data[int(max_child_index)] = tmp  # type: ignore
            index = int(max_child_index)  # type: ignore

    def peek(self):
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0
