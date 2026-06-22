from typing import Literal
import lab1.parse.parser as parser
import lab1.parse.validate as validate
from lab1.stack.stack import Stack


def eval(expression: str, expression_type: Literal["prefix", "postfix"]) -> int | None:
    # while input, read expression from right for prefix, from left for postfix
    # if operand push onto stack
    # if operation
    #    pop A
    #    pop B
    #    perform operation // A op B for prefix, B op A for postfix
    #    push result
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
