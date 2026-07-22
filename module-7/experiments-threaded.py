from typing import List, Any, Tuple


class Node:
    def __init__(self, data, right_thread=None):
        self.data = data if data else None
        self.right_thread = right_thread if right_thread else None
        self.right_is_thread = False

    def __repr__(self):
        return f"{{{self.data} {self.right_is_thread}:->> {self.right_thread}}}"


def extend_array(array):
    array = [] if array is None else array
    size = 1 if len(array) == 0 else len(array)
    new_array = []
    new_array.extend([None]*size*2)
    for i in range(size):
        new_array[i] = array[i]
    return new_array


def maketree(item: Any, tree_array: List, index: int) -> List:
    tree_array = [None] if tree_array is None else tree_array
    index = 0 if index is None else index
    node = Node(data=item)
    node.data = item
    node.right_thread = None
    if index >= len(tree_array):
        tree_array = extend_array(tree_array)
    tree_array[index] = node
    return tree_array


def parent_index(index: int) -> int | None:
    if index == 0:
        return None
    reduction = 2 if index % 2 == 0 else 1
    parent = (index - reduction) // 2
    return parent


def left_child_index(tree_array: List, index: int, write: bool = False) -> Tuple[List, int | None]:
    if index >= len(tree_array):
        return tree_array, None
    left_child_index = (index * 2) + 1
    if left_child_index >= len(tree_array):
        if write:
            tree_array = extend_array(tree_array)
            return tree_array, left_child_index
        else:
            return tree_array, None
    elif left_child_index < len(tree_array):
        return tree_array, left_child_index
    else:  # something went wrong
        return tree_array, None


def right_child_index(tree_array: List, index: int, write: bool = False) -> Tuple[List, int | None]:
    if index >= len(tree_array):
        return tree_array, None
    right_child_index = (index * 2) + 2
    if right_child_index >= len(tree_array):
        if write:
            tree_array = extend_array(tree_array)
            return tree_array, right_child_index
        else:
            return tree_array, None
    elif right_child_index < len(tree_array):
        return tree_array, right_child_index
    else:  # something went wrong
        return tree_array, None


def setleft(item: Any, tree_array: List, index: int) -> List:
    if index >= len(tree_array):
        raise IndexError(
            "Couldn't find node: That position doesn't exist in the tree")
    if tree_array[index] is None:
        raise ValueError(
            "Couldn't find node: That node doesn't exist in the tree")
    if not isinstance(tree_array[index], Node):
        raise ValueError(
            f"The tree was corrupted. Can't proceed. {tree_array[index]} is not a Node.")

    tree_array, lc_index = left_child_index(tree_array, index, write=True)
    if lc_index is None:  # left child index is out of range
        raise IndexError(
            "Couldn't find node: the provided position doesn't exist in the tree")

    # index is within range, possible that we have a node there
    if tree_array[lc_index] is not None:  # found a node alredy exists
        raise ValueError(
            "Cant set left child. The selected node already has a left child.")

    if tree_array[lc_index] is None:
        lc_node = Node(item)
        # set the current node's (i.e. the left child's parent) as the right thread
        lc_node.right_thread = index
        lc_node.right_is_thread = True
        tree_array[lc_index] = lc_node

    return tree_array


def setright(item: Any, tree_array: List, index: int) -> List:
    if index >= len(tree_array):
        raise IndexError(
            "Couldn't find node: That position doesn't exist in the tree")
    if tree_array[index] is None:
        raise ValueError(
            "Couldn't find node: That node doesn't exist in the tree")
    if not isinstance(tree_array[index], Node):
        raise ValueError(
            f"The tree was corrupted. Can't proceed. {tree_array[index]} is not a Node.")

    parent_node = tree_array[index]
    tree_array, rc_index = right_child_index(tree_array, index, write=True)
    if rc_index is None:  # right child index is out of range
        raise IndexError(
            "Couldn't find node: the provided position doesn't exist in the tree")

    # index is within range, possible that we have a node there
    if tree_array[rc_index] is not None:  # found a node alredy exists
        raise ValueError(
            "Cant set right child. The selected node already has a right child.")

    if tree_array[rc_index] is None:
        rc_node = Node(item)
        # copy the right thread pointer from the parent
        rc_node.right_thread = parent_node.right_thread
        rc_node.right_is_thread = True
        # parent's successor thread points to the right child
        parent_node.right_thread = rc_index
        parent_node.right_is_thread = False
        tree_array[index] = parent_node
        tree_array[rc_index] = rc_node

    return tree_array


def get_leftmost_descendant(tree_array, index) -> Tuple[Node, int]:
    tree_array, lc_index = left_child_index(tree_array, index, write=False)
    if lc_index is None:
        return tree_array[index], index
    # left subtree
    leftmost_descendant = None
    while True:
        if lc_index is None:
            return leftmost_descendant, index  # type:ignore
        if tree_array[lc_index] is None:
            return leftmost_descendant, index  # type:ignore
        index = lc_index
        leftmost_descendant = tree_array[index]
        tree_array, lc_index = left_child_index(tree_array, index, write=False)


def traverse_inorder(tree_array: List, index: int = 0, visit=print):
    if len(tree_array) == 0:
        return
    if len(tree_array) == 1:
        visit(tree_array[0])
        return
    current_node, index = get_leftmost_descendant(
        tree_array, index)  # type:ignore
    while True:
        if current_node is None:
            raise ValueError
        visit(current_node)
        if current_node.right_thread is None:
            return
        if current_node.right_is_thread:
            index = current_node.right_thread
            current_node = tree_array[index]
        else:
            tree_array, rc_index = right_child_index(tree_array, index)
            current_node, index = get_leftmost_descendant(
                tree_array, rc_index)  # type:ignore


def __main__():
    a = maketree(item="H", tree_array=None, index=0)  # type:ignore
    a = setleft("D", a, 0)
    a = setright("L", a, 0)
    a = setleft("B", a, 1)
    a = setright("F", a, 1)
    a = setleft("J", a, 2)
    a = setright("N", a, 2)
    a = setleft("A", a, 3)
    a = setright("C", a, 3)
    a = setleft("E", a, 4)
    a = setright("G", a, 4)
    a = setleft("I", a, 5)
    a = setright("K", a, 5)
    a = setleft("M", a, 6)
    a = setright("O", a, 6)

    # [print(i, x) for i, x in enumerate(a)]
    traverse_inorder(a, 0, visit=print)
    # assert parent_index((parent_index(2) * 2) +
    #                     2) == parent_index(2)  # type:ignore


if __name__ == "__main__":
    __main__()
