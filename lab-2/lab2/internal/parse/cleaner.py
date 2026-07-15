import lab2.internal.parse.validate as validate


def clean(expression: str) -> str:
    """Returns copy of expression with irrelevant characters removed

    Args:
        expression: str a candidate prefix expression

    Returns:
        A copy of expression with irrelevant characters removed

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        True
    """
    characters = []
    for s in expression:
        if validate.is_whitespace(s):
            continue
        if validate.is_allowed(s):
            characters.append(s)
            continue
    cleaned_expression = "".join(characters)
    return cleaned_expression
