from typing import Literal
import lab1.parse.parser as parser
from lab1.stack.stack import Stack


def is_valid_expression(expression: str, expression_type: Literal["prefix", "postfix"]) -> bool:
    """Returns a boolean indicating whether a provided expression is valid

    Performs a validation that the provided expression is in a valid prefix or postfix
    form, according to the value of expression_type. Returns true if valid, false if not.

    Args:
        expression: str where expression is a sequence of operations and operands
        listed in prefix or postfix order, such as +AB or AB+ to represent the
        infix expression A+B
        
        expression_type: one of the two strings 'prefix' or 'postfix', controlling
        the algorithms for validating and evaluating the expressions

    Returns:
        A bool indicating whether the expression is valid in the form specified
    
    Raises:
        ValueError: if the expression cannot be parsed

    Side Effects:
        Raises ValueError as described above
    
    Idempotent:
        True
    """
    try:
        parsed_expression = parser.parse(expression=expression,
                                         translate_symbols=True)
    except ValueError:
        return False

    # short circuit to save time if singleton
    if is_singleton_operand(parsed_expression):
        return True

    if expression_type == "prefix":
        iterate_from_left = False
        opening_parens = ")"
        closing_parens = "("
        if is_start_of_expression_an_operand(parsed_expression):
            return False  # Prefix expressions can't start with operand
    if expression_type == "postfix":
        iterate_from_left = True
        opening_parens = "("
        closing_parens = ")"

    num_operators = 0
    num_operands = 0
    stack = Stack()
    parentheses_stack = Stack()
    # check expression
    for i in range(0, len(parsed_expression)):
        if iterate_from_left:
            index = i
        if not iterate_from_left:
            index = len(parsed_expression) - (i + 1)
        symbol = parsed_expression[index]
        # reject expressions with whitespace
        if is_whitespace(symbol):
            return False
        # handle parentheses balancing
        if symbol == opening_parens:
            parentheses_stack.push(symbol)
        if symbol == closing_parens:
            if parentheses_stack.peek() == opening_parens:
                _ = parentheses_stack.pop()
            else:
                return False  # unbalanced
        # handle operands
        if isinstance(symbol, int):
            num_operands += 1
            stack.push(symbol)
        # handle operators
        if is_operator(str(symbol)):
            a = stack.pop()
            b = stack.pop()
            if not isinstance(a, int) or not isinstance(b, int):
                return False
            if expression_type == "prefix":  # A op B
                res = parser.execute_operation(symbol, a, b)  # type: ignore
            if expression_type == "postfix":  # B op A
                res = parser.execute_operation(symbol, b, a)  # type: ignore
            stack.push(res)
            num_operators += 1
    # final result calculated
    if stack.height == 1 and isinstance(stack.peek(), int):
        return True
    # unbalanced parentheses
    if not parentheses_stack.is_empty():
        return False
    # empty expressions -> valid as empty case
    if stack.is_empty() and num_operators == 0 and num_operands <= 1:
        return True
    # imbalance of operators to operands
    if num_operators != (num_operands - 1):
        return False
    return True


def is_singleton_operand(parsed_expression: list) -> bool:
    """Returns a boolean indicating whether the expression is a single operand

    Returns true if the parsed expression is an int or single capital ascii letter,
    which should be interpreted as a valid prefix or postfix expression

    Args:
        parsed_expression: list representation of an expression

    Returns:
        A bool indicating whether the expression is a single operand
    
    Raises:
        ValueError: if the expression cannot be parsed

    Side Effects:
        Raises ValueError as described above
    
    Idempotent:
        True
    """
    if not isinstance(parsed_expression, list):
        raise ValueError(f"Could not read parsed expression. Expected list, but got {type(parsed_expression)}")
    if not parsed_expression:
        return False
    if len(parsed_expression) == 1:
        symbol = parsed_expression[0]
        if isinstance(symbol, int):
            return True
        is_capital_ascii_letter = (ord(symbol) >= 65 and ord(symbol) <= 90)
        if is_capital_ascii_letter:
            return True
    return False


def is_start_of_expression_an_operand(parsed_expression: list) -> bool:
    """Returns a boolean indicating whether the expression starts with operand

    Returns true if the parsed expression list begins with an operand. This is
    used in determining validity for expressions.

    Args:
        parsed_expression: list representation of an expression

    Returns:
        A bool indicating whether the expression begins with an operand
    
    Raises:
        ValueError: if the expression cannot be parsed

    Side Effects:
        Raises ValueError as described above
    
    Idempotent:
        True
    """
    if not isinstance(parsed_expression, list):
        raise ValueError(f"Could not read parsed expression. Expected list, but got {type(parsed_expression)}")
    if not parsed_expression:
        return False
    symbol = parsed_expression[0]
    if is_capital_ascii_letter(symbol):
        return True
    if isinstance(symbol, int):
        return True
    return False


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


def is_capital_ascii_letter(symbol: str) -> bool:
    if not isinstance(symbol, str):
        return False
    return (ord(symbol) >= 65 and ord(symbol) <= 90)


def is_operator_or_bracket(symbol: str) -> bool:
    if not isinstance(symbol, str):
        return False
    return (symbol in ["+", "-", "*", "/", "$", "(", ")"])


def is_allowed(symbol: str) -> bool:
    if not isinstance(symbol, str):
        return False
    if is_operator_or_bracket(symbol) or is_capital_ascii_letter(symbol):
        return True
    return False
