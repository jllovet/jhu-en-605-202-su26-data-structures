from typing import List, Any, Tuple


class Node:
    def __init__(self, data, right_thread=None):
        self.data = data if data else None
        self.right_thread = right_thread if right_thread else None

    def __repr__(self):
        return f"{{{self.data} t:->> {self.right_thread}}}"


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


def left_child_index(tree_array: List, index: int) -> Tuple[List, int | None]:
    if index >= len(tree_array):
        raise IndexError("Couldn't find node: the provided position doesn't exist in the tree")
    left_child_index = (index * 2) + 1
    if left_child_index >= len(tree_array):
        tree_array = extend_array(tree_array)
        return tree_array, left_child_index
    elif left_child_index < len(tree_array):
        return tree_array, left_child_index
    else: # something went wrong
        return tree_array, None


def right_child_index(tree_array: List, index: int) -> Tuple[List, int | None]:
    if index >= len(tree_array):
        return tree_array, None
    right_child_index = (index * 2) + 2
    if right_child_index >= len(tree_array):
        tree_array = extend_array(tree_array)
        return tree_array, right_child_index
    elif right_child_index < len(tree_array):
        return tree_array, right_child_index
    else: # something went wrong
        return tree_array, None


def setleft(item: Any, tree_array: List, index: int) -> List:
    if index >= len(tree_array):
        raise IndexError("Couldn't find node: That position doesn't exist in the tree")
    if tree_array[index] is None:
        raise ValueError("Couldn't find node: That node doesn't exist in the tree")
    if not isinstance(tree_array[index], Node):
        raise ValueError(f"The tree was corrupted. Can't proceed. {tree_array[index]} is not a Node.")
    
    tree_array, lc_index = left_child_index(tree_array, index)
    if lc_index is None: # left child index is out of range
        raise IndexError("Couldn't find node: the provided position doesn't exist in the tree")
    
    # index is within range, possible that we have a node there
    if tree_array[lc_index] is not None: # found a node alredy exists
        raise ValueError("Cant set left child. The selected node already has a left child.")
    
    if tree_array[lc_index] is None:
        lc_node = Node(item)
        lc_node.right_thread = index # set the current node's (i.e. the left child's parent) as the right thread
        tree_array[lc_index] = lc_node

    return tree_array


def setright(item: Any, tree_array: List, index: int) -> List:
    if index >= len(tree_array):
        raise IndexError("Couldn't find node: That position doesn't exist in the tree")
    if tree_array[index] is None:
        raise ValueError("Couldn't find node: That node doesn't exist in the tree")
    if not isinstance(tree_array[index], Node):
        raise ValueError(f"The tree was corrupted. Can't proceed. {tree_array[index]} is not a Node.")
    
    parent_node = tree_array[index]
    tree_array, rc_index = right_child_index(tree_array, index)
    if rc_index is None: # right child index is out of range
        raise IndexError("Couldn't find node: the provided position doesn't exist in the tree")
    
    # index is within range, possible that we have a node there
    if tree_array[rc_index] is not None: # found a node alredy exists
        raise ValueError("Cant set right child. The selected node already has a right child.")
    
    if tree_array[rc_index] is None:
        rc_node = Node(item)
        rc_node.right_thread = parent_node.right_thread # copy the right thread pointer from the parent
        # parent is no longer threaded, because it has this new node as an explicit successor
        parent_node.right_thread = None
        tree_array[index] = parent_node
        tree_array[rc_index] = rc_node

    return tree_array


def __main__():
    a = maketree(item=14, tree_array=None, index=0)  # type:ignore
    a = setleft(123, a, 0)
    print(a)
    a = setright("abc", a, 0)
    a = setright("m", a, 1)
    a = setleft("m", a, 1)
    print(a)
    assert parent_index((parent_index(2) * 2) + 2) == parent_index(2) #type:ignore


if __name__ == "__main__":
    __main__()
