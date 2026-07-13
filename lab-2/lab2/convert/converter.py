from lab2.stack.stack import Stack
import lab2.parse.parser as parser
import lab2.parse.validate as validate
from typing import Tuple, Optional

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
    # print(f"in pre2post({expression, index})")
    if index == len(expression):
        return None, index
    while index <= len(expression) - 1 and (expression[index].isspace() or validate.is_parenthesis(expression[index])):
        print(index)
        index += 1
    # print(
        # f"after char skip loop in pre2post({expression, len(expression), index})")
    n = Node(expression[index])
    # print(f"created node: {n}")
    if validate.is_operator(expression[index]):
        left, index = _pre2post(expression, index+1)
        right, index = _pre2post(expression, index+1)
        n.left = left
        n.right = right
    if expression[index].isalpha():
        pass
    return n, index


def pre2post(expression: str) -> str:
    """Converts a prefix expression to a postfix expression

    Performs a validation that the provided expression is in a valid prefix form.
    If it is not, then a ValueError is raised. Otherwise, it converts the
    prefix expression to an equivalent postfix expression.

    Args:
        expression: str where expression is a sequence of operations and operands
        listed in prefix order, such as +AB to represent the infix expression A+B

    Returns:
        A str containing the postfix expression equivalent to the expression provided

    Raises:
        ValueError: if the expression is not a valid prefix expression

    Side Effects:
        Raises ValueError if the expression provided was not valid

    Idempotent:
        True
    """
    if not validate.is_valid_expression(expression=expression, expression_type="prefix"):
        raise ValueError(f"'{expression}' is not a valid prefix expression")
    # Passing here -> parentheses are balanced
    # We actually don't need to handle them at all for this conversion,
    # since precedence is explicit in prefix and postfix expressions.
    # stack = Stack()
    # parsed_expression = parser.parse(expression=expression)
    # postfix_expression_components = []
    # if parsed_expression == [] or len(parsed_expression) == 1:
    #     return expression
    # for i in range(0, len(parsed_expression)):  # iterate from right
    #     index = len(parsed_expression) - (i + 1)
    #     symbol = parsed_expression[index]
    #     if validate.is_parenthesis(symbol):
    #         continue
    #     if validate.is_operator(str(symbol)):
    #         a = stack.pop()
    #         b = stack.pop()
    #         stack.push(f"{a}{b}{symbol}")
    #     elif isinstance(symbol, str):
    #         stack.push(symbol)
    # while not stack.is_empty():
    #     symbol = stack.pop()
    #     postfix_expression_components.append(symbol)
    # postfix_expression = "".join(postfix_expression_components)
    # return postfix_expression
    tree, _ = _pre2post(expression=expression, index=0)
    if tree:
        return "".join(n for n in tree)
    else:
        return ""
