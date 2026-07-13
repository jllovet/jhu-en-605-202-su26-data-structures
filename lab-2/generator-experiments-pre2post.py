from typing import Tuple, Optional


def is_operator(symbol: str) -> bool:
    """Returns a boolean indicating whether the symbol is an operator

    Returns true if the symbol is in one of the operators: +, -, *, /, $

    Args:
        symbol: str a single character from an expression

    Returns:
        A bool indicating whether the symbol is an operator

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        True
    """
    if not isinstance(symbol, str):
        return False
    match symbol:
        case "+":
            return True
        case "-":
            return True
        case "/":
            return True
        case "*":
            return True
        case "$":
            return True
    return False


def is_operator_or_bracket(symbol: str) -> bool:
    """Returns a boolean indicating whether the symbol is an operator or parenthesis

    Returns true if the symbol is any of +, -, *, /, $, (, )

    Args:
        symbol: str a single character from an expression

    Returns:
        A bool indicating whether the symbol is any of +, -, *, /, $, (, )

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        True
    """
    if not isinstance(symbol, str):
        return False
    return (symbol in ["+", "-", "*", "/", "$", "(", ")"])


def is_parenthesis(symbol: str) -> bool:
    """Returns a boolean indicating whether the symbol is "(" or ")"

    Args:
        symbol: str a single character from an expression

    Returns:
        A bool indicating whether the symbol is a parenthesis

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        True
    """
    return symbol == "(" or symbol == ")"


class Node:
    def __init__(self, data, left=None, right=None):
        self.data: str = data
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def __str__(self):
        return f"{self.data}"
        # return f"{self.data}, left: {self.left}, right: {self.right}"

    def __iter__(self):
        if self.left:
            yield from self.left
        if self.right:
            yield from self.right
        yield self.data


def _pre2post(expression: str, index: int = 0) -> Tuple[Node, int] | Tuple[None, int]:
    print(f"in pre2post({expression, index})")
    if index == len(expression):
        return None, index
    while index <= len(expression) - 1 and (expression[index].isspace() or is_parenthesis(expression[index])):
        print(index)
        index += 1
    print(
        f"after char skip loop in pre2post({expression, len(expression), index})")
    n = Node(expression[index])
    print(f"created node: {n}")
    if is_operator(expression[index]):
        left, index = _pre2post(expression, index+1)
        right, index = _pre2post(expression, index+1)
        n.left = left
        n.right = right
    if expression[index].isalpha():
        pass
    return n, index


def tree2str(tree) -> str:
    if tree:
        return "".join(n for n in tree)
    else:
        return ""


tree, _ = _pre2post(expression="  ()) (+AB)", index=0)
print(tree2str(tree))

