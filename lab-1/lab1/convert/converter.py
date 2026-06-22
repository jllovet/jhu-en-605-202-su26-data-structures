from lab1.stack.stack import Stack
import lab1.parse.parser as parser
import lab1.parse.validate as validate


def pre2post(expression: str) -> str:
    """Converts a prefix expression to a postfix expression

    Performs a validation that the provided expression is in a valid prefix form.
    If it is not, then a ValueError is raised. Otherwise, it converts the
    prefix expression to an equivalent postfix expression.

    Args:
        expression: str where expression is a sequence of operations and operands
        listed in prefix order, such as +AB to represent the infix expression A+B

    Returns:
        A str containing the postfix expression equivalent to the expression provided
    
    Raises:
        ValueError: if the expression is not a valid prefix expression

    Side Effects:
        Raises ValueError if the expression provided was not valid
    
    Idempotent:
        True
    """
    if not validate.is_valid_expression(expression=expression, expression_type="prefix"):
        raise ValueError(f"'{expression}' is not a valid prefix expression")
    # Passing here -> parentheses are balanced
    # We actually don't need to handle them at all for this conversion,
    # since precedence is explicit in prefix and postfix expressions.
    stack = Stack()
    parsed_expression = parser.parse(expression=expression)
    postfix_expression_components = []
    if parsed_expression == [] or len(parsed_expression) == 1:
        return expression
    for i in range(0, len(parsed_expression)):  # iterate from right
        index = len(parsed_expression) - (i + 1)
        symbol = parsed_expression[index]
        if validate.is_parentheses(symbol):
            continue
        if validate.is_operator(str(symbol)):
            a = stack.pop()
            b = stack.pop()
            stack.push(f"{a}{b}{symbol}")
        elif isinstance(symbol, str):
            stack.push(symbol)
    while not stack.is_empty():
        symbol = stack.pop()
        postfix_expression_components.append(symbol)
    postfix_expression = "".join(postfix_expression_components)
    return postfix_expression
