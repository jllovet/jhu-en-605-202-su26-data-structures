def lookup_symbol(symbol: str) -> int | str:
    if not symbol:
        return ""
    if ord(symbol) >= 65 and ord(symbol) <= 90:  # operands A - Z
        return ord(symbol) - 64
    else:
        return symbol


def parse(expression) -> list:
    parsed_symbols = []
    for s in expression:
        parsed_symbols.append(lookup_symbol(s))
    return parsed_symbols


def is_valid_prefix_expression(parsed_expression: list) -> bool:
    if len(parsed_expression) == 1 and isinstance(parsed_expression[0], int):
        return True
    return False

def is_valid_postfix_expression(parsed_expression: list) -> bool:
    if len(parsed_expression) == 1 and isinstance(parsed_expression[0], int):
        return True
    return False


def evaluate_postfix(expression: str) -> int | None:
    parsed_expression = parse(expression=expression)
    if parsed_expression == []:
        return None
    if not is_valid_prefix_expression(parsed_expression):
        raise ValueError(f"{expression} is not a valid prefix expression")
    return parsed_expression[0]
    # while input, read expression from left
    # if operand push onto stack
    # if operation
        # pop A
        # pop B
        # perform operation // B op A
        # push result

def evaluate_prefix(expression: str) -> int | None:
    parsed_expression = parse(expression=expression)
    if parsed_expression == []:
        return None
    if not is_valid_postfix_expression(parsed_expression):
        raise ValueError(f"{expression} is not a valid postfix expression")
    return parsed_expression[0]
    # while input, read expression from right
    # if operand push onto stack
    # if operation
        # pop A
        # pop B
        # perform operation // A op B
        # push result

