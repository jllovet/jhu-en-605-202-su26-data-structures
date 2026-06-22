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

def is_allowed(symbol: str) -> bool:
    if not isinstance(symbol, str):
        return False
    is_capital_ascii_letter = (ord(symbol) >= 65 and ord(symbol) <= 90)
    is_operator_or_bracket = (symbol in ["+", "-", "*", "/", "$", "(", ")"])
    if is_operator_or_bracket or is_capital_ascii_letter:
        return True
    return False
