from lab1.stack import Stack


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


def execute_operation(s: str, a: int, b: int) -> int:
    match s:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a // b
        case "$":
            return a ** b
    raise ValueError(
        f"Unable to execute operation {a}{s}{b}, because {s} was not recognized")

