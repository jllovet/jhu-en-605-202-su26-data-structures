import lab2.parse.validate as validate


def lookup_symbol(symbol: str) -> int | str:
    """Converts operands from expression into ints and returns operators unchanged

    Converts operand values for uppercase ascii characters into a corresponding
    int value, with A -> 1, B -> 2, ... Z -> 26. Other characters, representing
    operations and parentheses, are not modified and are returned as str values.

    Args:
        symbol: str where symbol is one of the characters from an expression

    Returns:
        An int A -> 1, B -> 2, ... Z -> 26 or the original str symbol

    Raises:
        ValueError: None

    Side Effects:
        None

    Idempotent:
        True
    """
    if not symbol:
        return ""
    if ord(symbol) >= 65 and ord(symbol) <= 90:  # operands A - Z
        return ord(symbol) - 64
    else:
        return symbol


def parse(expression: str, translate_symbols: bool = False) -> list:
    """Converts an expression into a list of symbols, with optional replacement

    Returns a list representing the original expression broken into individual
    symbols. If translate_symbols is True, then the symbols for operands are
    replaced with their equivalent int values. If translate_symbols is False,
    then the symbols for operands are not replaced. Raises a ValueError if the
    expression contains illegal characters.

    Examples:
    parse("+AB", True)  -> ["1","2","+"]
    parse("+AB", False) -> ["A","B","+"]

    Args:
        expression: str where expression is a sequence of operations and operands

    Returns:
        list of the symbols in the expression, with operands translated to ints
        depending on the value of translate_symbols

    Raises:
        ValueError: if the expression contains illegal characters

    Side Effects:
        Raises ValueError as described above

    Idempotent:
        True
    """
    parsed_symbols = []
    for symbol in expression:
        if not validate.is_allowed(symbol):
            raise ValueError(
                f"Could not parse {expression} because it contains illegal character: '{symbol}'")
        if translate_symbols:
            parsed_symbols.append(lookup_symbol(symbol))
        if not translate_symbols:
            parsed_symbols.append(symbol)
    return parsed_symbols
