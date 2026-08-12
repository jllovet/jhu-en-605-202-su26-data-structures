from typing import List, Tuple
from lab4.sort.context import Context, Algorithm, NaturalMergeSort

import logging
logger = logging.getLogger(__name__)


class Node:
    def __init__(self, data: int, pos: int, prev: Node | None = None, next: Node | None = None):
        """Initializes a Node object

        Args:
            data: int the information stored in the Node
            pos: int position in the list, to be used for inspection
            prev: Node | None a pointer to a previous Node
            next: Node | None a pointer to a subsequent Node

        Returns:
            None

        Raises:
            None

        Side Effects:
            Initializes a Node object

        Idempotent:
            True
        """
        self.data = data
        self.pos = pos
        self.prev = prev
        self.next = next

    def __repr__(self):
        """Returns a str representation of the node"""
        return f"{self.data}, pos: {self.pos}, next: {self.next}"

    def __le__(self, other):
        """Returns a boolean indicating whether the data of one node is less than or equal to the data of another"""
        return self.data <= other.data

    def __lt__(self, other):
        """Returns a boolean indicating whether the data of one node is less than the data of another"""
        return self.data < other.data

    def __ge__(self, other):
        """Returns a boolean indicating whether the data of one node is greater than or equal to the data of another"""
        return self.data >= other.data

    def __gt__(self, other):
        """Returns a boolean indicating whether the data of one node is greater than the data of another"""
        return self.data > other.data


class LinkedList:
    def __init__(self):
        """Initializes a Linked List by setting the head to None"""
        self.head: Node | None = None

    def as_list(self):
        """Returns a list/array representation of the linked list"""
        xs = []
        if self.head is None:
            return []
        else:
            current = self.head
        xs.append(current.data)
        while current.next is not None:
            current = current.next
            xs.append(current.data)
        return xs


def get_sorted_segment(context: Context, xsLLNode: Node) -> Tuple[Context, int, Node]:
    """Returns the context, the length of the sorted segment of nodes, and the last node of the segment"""
    current = xsLLNode
    length_of_segment = 1
    next = current.next
    if next is None:
        return context, length_of_segment, current
    while next is not None:
        context.comparisons += 1
        if current.data <= next.data:
            length_of_segment += 1
            current = next
            next = current.next
        else:
            break
    return context, length_of_segment, current


def linked_natural_merge_sort(context: Context, xs: List[int]) -> Tuple[Context, List[int]]:
    """Sorts a list using natural merge sort"""
    xsLL = LinkedList()
    xsLL.head = Node(xs[0], 0)
    prev = xsLL.head
    for i in range(1, len(xs)):
        n = Node(data=xs[i], pos=i, prev=prev, next=None)
        prev.next = n
        prev = n
    logger.debug(xsLL.head)
    # segment_heads = []
    beginning_of_segment_a = xsLL.head
    while beginning_of_segment_a.next is not None:
        # Segment A
        logger.debug(f"beginning of segment: {beginning_of_segment_a}")
        context, length_of_sorted_segment_a, end_of_segment_a = get_sorted_segment(
            context=context, xsLLNode=beginning_of_segment_a)
        logger.debug(f"end of segment A: {end_of_segment_a}")
        if end_of_segment_a.next is None:
            break

        # Segment B
        if end_of_segment_a.next is not None:
            beginning_of_segment_b = end_of_segment_a.next
            context, length_of_sorted_segment_b, end_of_segment_b = get_sorted_segment(
                context=context, xsLLNode=beginning_of_segment_b)
            logger.debug(f"beginning_of_segment_b: {beginning_of_segment_b}")
            logger.debug(f"end_of_segment B: {end_of_segment_b}")

        context, head_a = merge_segments(context,
                                         head_a=beginning_of_segment_a,
                                         end_of_segment_a=end_of_segment_a,
                                         head_b=beginning_of_segment_b,
                                         end_of_segment_b=end_of_segment_b)
        logger.debug(f"result of merging: {head_a}")
        if end_of_segment_b.next is not None:
            beginning_of_segment_a = end_of_segment_b.next
        else:
            # Loop back around to the beginning
            logger.debug(
                f"Loop back around to the beginning: {xsLL.as_list()}")
            beginning_of_segment_a = xsLL.head

    return context, xsLL.as_list()


def merge_segments(context: Context, head_a: Node, end_of_segment_a: Node, head_b: Node, end_of_segment_b: Node) -> Tuple[Context, Node]:
    """Merges two linked segments into a sorted linked list"""
    # This is currently not working. Will need to think more about how to wire the pointers together
    a_current = head_a
    b_current = head_b
    current = a_current if a_current <= b_current else b_current
    context.comparisons += 1
    if current is a_current:
        a_current = a_current.next
    elif current is b_current:
        b_current = b_current.next
    logger.debug(f"head_a at start: {head_a.data}")
    logger.debug(f"head_b at start: {head_b.data}")
    while a_current is not end_of_segment_a.next and b_current is not end_of_segment_b.next:
        next = a_current if a_current is not None and a_current <= b_current else b_current
        context.comparisons += 1
        if current is a_current:
            a_current = a_current.next  # type: ignore
        elif current is b_current:
            b_current = b_current.next  # type: ignore
        current.next = next
    logger.debug(
        f"attempted to merge segments A and B! head_a: {head_a.data}")
    return context, head_a


def sort(xs: List[int], algorithm: Algorithm = NaturalMergeSort) -> Tuple[Context, List[int]]:
    """Performs a linked natural merge sort on a list"""
    context = Context(algorithm=algorithm, xs=xs)
    if len(xs) < 2:
        return context, xs
    else:
        return linked_natural_merge_sort(context=context, xs=xs)
