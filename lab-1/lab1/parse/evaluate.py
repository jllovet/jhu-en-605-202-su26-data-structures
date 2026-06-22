from typing import Literal
import lab1.parse.parser as parser
import lab1.parse.validate as validate
from lab1.stack.stack import Stack


def eval(expression: str, expression_type: Literal["prefix", "postfix"]) -> int | None:
    """Evaluates the expression according to the algorithm appropriate for its type

    Performs smybolic replacement of the symbols provided in the expression and
    then evaluates the mathematical expression, returning the result as an int if
    a result is calculated or returning None if the expression is empty. This function
    is available as a way to determine that two expressions pre and post conversion
    return the same values. If a postfix expression is equivalent to a prefix
    expression, then eval should return the same value on each of them.

    The algorithm for evaluation is as follows (adapted from course slides):

    while input, read symbol from expression from right for prefix, from left for postfix
        if symbol is operand push symbol onto stack
        if symbol is operation
           A <- pop from stack
           B <- pop from stack
           result <- perform operation A op B for prefix, B op A for postfix
           push result onto stack

    Args:
        expression: str where expression is a sequence of operations and operands
        listed in prefix or postfix order, such as +AB or AB+ to represent the
        infix expression A+B
        expression_type: one of the two strings 'prefix' or 'postfix', controlling
        the algorithms for validating and evaluating the expressions

    Returns:
        An int containing the result of the evaluation or None if the expression
        is empty

    Raises:
        ValueError: if the expression is not a valid prefix or postfix expression
        ValueError: if the evaluation does not produce an integer

    Side Effects:
        Raises ValueError in cases described above

    Idempotent:
        True
    """
    if expression_type == "prefix":
        iterate_from_left = False
    if expression_type == "postfix":
        iterate_from_left = True
    if not validate.is_valid_expression(expression, expression_type):
        raise ValueError(
            f"{expression} is not a valid {expression_type} expression")
    parsed_expression = parser.parse(
        expression=expression, translate_symbols=True)
    if parsed_expression == []:
        return None
    stack = Stack()
    for i in range(0, len(parsed_expression)):
        if iterate_from_left:
            index = i
        if not iterate_from_left:
            index = len(parsed_expression) - (i + 1)
        symbol = parsed_expression[index]
        if isinstance(symbol, int):
            stack.push(symbol)
        if validate.is_operator(str(symbol)):
            a = stack.pop()
            b = stack.pop()
            if expression_type == "prefix":  # A op B
                res = parser.execute_operation(symbol, a, b)  # type: ignore
            if expression_type == "postfix":  # B op A
                res = parser.execute_operation(symbol, b, a)  # type: ignore
            stack.push(res)
    if isinstance(stack.peek(), int):
        return stack.pop()  # type: ignore
    else:
        raise ValueError(f"Could not evaluate {expression}")
