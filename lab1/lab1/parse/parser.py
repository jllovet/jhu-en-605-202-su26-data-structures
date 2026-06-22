def lookup_symbol(symbol: str) -> int | str:
    if not symbol:
        return ""
    if ord(symbol) >= 65 and ord(symbol) <= 90:  # operands A - Z
        return ord(symbol) - 64
    else:
        return symbol


def parse(expression, translate_symbols: bool = False) -> list:
    parsed_symbols = []
    for s in expression:
        if not isinstance(s, str) \
                or (ord(s) < 65 or ord(s) > 90) \
                and s not in ["+", "-", "*", "/", "$", "(", ")"]:
            raise ValueError(
                f"Could not parse {expression} because it contains illegal character: '{s}'")
        if translate_symbols:
            parsed_symbols.append(lookup_symbol(s))
        if not translate_symbols:
            parsed_symbols.append(s)
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
