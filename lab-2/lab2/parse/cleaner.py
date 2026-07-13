import lab2.parse.validate as validate

def clean(expression: str) -> str:
    characters = []
    for s in expression:
        if validate.is_whitespace(s):
            continue
        if validate.is_allowed:
            characters.append(s)
            continue
    cleaned_expression = "".join(characters)
    return cleaned_expression
