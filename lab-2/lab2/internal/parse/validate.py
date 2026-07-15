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


def is_operand(symbol: str) -> bool:
    """Returns a boolean indicating whether the symbol is an operand

    Returns true when symbol.islpha() is True

    Args:
        symbol: str a single character from an expression

    Returns:
        A bool indicating whether the symbol is an operand

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        True
    """
    if not isinstance(symbol, str):
        return False
    return symbol.isalpha()


def is_whitespace(symbol: str) -> bool:
    """Returns a boolean indicating whether the symbol is whitespace

    Returns true when symbol.isspace() is True

    Args:
        symbol: str a single character from an expression

    Returns:
        A bool indicating whether the symbol is whitespace

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        True
    """
    if not isinstance(symbol, str):
        return False
    return symbol.isspace()


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


def is_allowed(symbol: str) -> bool:
    """Returns a boolean indicating whether the symbol is allowed

    Returns true if the symbol is an operator or parenthesis or any
    character for which str.isalpha returns true

    Args:
        symbol: str a single character from an expression

    Returns:
        A bool indicating whether the symbol is operator or parenthesis
        or any of A,B,C...,X,Y,Z

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        True
    """
    if not isinstance(symbol, str):
        return False
    if is_operator_or_bracket(symbol) or symbol.isalpha():
        return True
    return False
