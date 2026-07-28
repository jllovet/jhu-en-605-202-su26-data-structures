from typing import Optional

class EncodingData:
    """Representation of data for encoding. Contains characters and score.
    Comparison prioritizes score, then length, then alphabetic order.
    """
    def __init__(self, characters:str, score:int):
        self.characters = characters
        self.score = score

    def __eq__(self, other: EncodingData) -> bool:
        same_score = self.score == other.score
        same_characters = self.characters == other.characters
        return same_score and same_characters

    def __lt__(self, other):
        # Sorting: score has highest priority, then length, then alphabetic order
        # Score
        if self.score < other.score:
            return True
        if self.score > other.score:
            return False
        # implies that self.score == other.score
        # Length
        if len(self.characters) < len(other.characters):
            return True
        if len(self.characters) > len(other.characters):
            return False
        # implies len(self.characters) == len(other.characters)
        # Alphabetic order
        return self.characters < other.characters

    def __gt__(self, other: EncodingData) -> bool:
        # Sorting: score has highest priority, then length, then alphabetic order
        # Score
        if self.score < other.score:
            return False
        if self.score > other.score:
            return True
        # implies that self.score == other.score
        # Length
        if len(self.characters) < len(other.characters):
            return False
        if len(self.characters) > len(other.characters):
            return True
        # implies len(self.characters) == len(other.characters)
        # Alphabetic order
        return self.characters > other.characters

    def __le__(self, other):
        # Sorting: score has highest priority, then length, then alphabetic order
        # Score
        if self.score <= other.score:
            return True
        if self.score > other.score:
            return False
        # implies that self.score == other.score
        # Length
        if len(self.characters) <= len(other.characters):
            return True
        if len(self.characters) > len(other.characters):
            return False
        # implies len(self.characters) == len(other.characters)
        # Alphabetic order
        return self.characters <= other.characters

    def __ge__(self, other: EncodingData) -> bool:
        # Sorting: score has highest priority, then length, then alphabetic order
        # Score
        if self.score < other.score:
            return False
        if self.score >= other.score:
            return True
        # implies that self.score == other.score
        # Length
        if len(self.characters) < len(other.characters):
            return False
        if len(self.characters) >= len(other.characters):
            return True
        # implies len(self.characters) == len(other.characters)
        # Alphabetic order
        return self.characters >= other.characters

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
