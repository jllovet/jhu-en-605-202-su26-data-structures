from typing import Literal
import lab1.parse.parser as parser
from lab1.stack.stack import Stack



def is_valid_expression(expression: str, expression_type: Literal["prefix", "postfix"]) -> bool:
    try:
        parsed_expression = parser.parse(expression=expression,
                                         translate_symbols=True)
    except ValueError:
        return False

    if len(parsed_expression) == 1:
        return isinstance(parsed_expression[0], int)

    if expression_type == "prefix":
        iterate_from_left = False
        opening_parens = ")"
        closing_parens = "("
    if expression_type == "prefix" and len(parsed_expression) > 1:
        if isinstance(parsed_expression[0], int):
            # Prefix expression can't start with operand
            return False
    if expression_type == "postfix":
        iterate_from_left = True
        opening_parens = "("
        closing_parens = ")"

    num_operations = 0
    num_operands = 0
    stack = Stack()
    parentheses_stack = Stack()

    def index(parsed_expression: list, i: int, iterate_from_left: bool) -> int:
        if iterate_from_left:
            return i
        if not iterate_from_left:
            return len(parsed_expression) - (i + 1)

    for i in range(0, len(parsed_expression)):
        idx = index(parsed_expression, i, iterate_from_left)
        symbol = parsed_expression[idx]
        if is_whitespace(symbol):
            return False
        if symbol == opening_parens:
            parentheses_stack.push(symbol)
        if symbol == closing_parens:
            if parentheses_stack.peek() == opening_parens:
                _ = parentheses_stack.pop()
            else:
                return False  # unbalanced
        if isinstance(symbol, int):
            num_operands += 1
            stack.push(symbol)
        if is_operation(str(symbol)):
            a = stack.pop()
            b = stack.pop()
            if not isinstance(a, int) or not isinstance(b, int):
                return False
            if expression_type == "prefix":
                res = parser.execute_operation(symbol, a, b)  # type: ignore
            if expression_type == "postfix":
                res = parser.execute_operation(symbol, b, a)  # type: ignore
            stack.push(res)
            num_operations += 1
    if stack.height == 1 and isinstance(stack.peek(), int):
        return True
    if not parentheses_stack.is_empty():
        return False
    if stack.is_empty() and num_operations == 0 and num_operands <= 1:
        return True
    if num_operations != (num_operands - 1):
        return False
    return True


def is_operation(symbol: str) -> bool:
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


def is_whitespace(symbol: str) -> bool:
    if not isinstance(symbol, str):
        return False
    match symbol:
        case " ":
            return True
        case "\t":
            return True
        case "\n":
            return True
        case "\v":
            return True
        case "\f":
            return True
    return False


def is_parentheses(symbol: str) -> bool:
    if symbol == "(" or symbol == ")":
        return True
    else:
        return False


def is_allowed(symbol: str) -> bool:
    if not isinstance(symbol, str):
        return False
    is_capital_ascii_letter = (ord(symbol) >= 65 and ord(symbol) <= 90)
    is_operator_or_bracket = (symbol in ["+", "-", "*", "/", "$", "(", ")"])
    if is_operator_or_bracket or is_capital_ascii_letter:
        return True
    return False
