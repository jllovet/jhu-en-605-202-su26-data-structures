import lab1.parse.validate as validate
from lab1.parse.evaluate import eval


def is_valid(expression: str) -> bool:
    return validate.is_valid_expression(expression=expression, expression_type="prefix")


def evaluate(expression: str) -> int | None:
    return eval(expression, "prefix")
