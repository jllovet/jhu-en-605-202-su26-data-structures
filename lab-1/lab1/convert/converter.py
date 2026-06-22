from lab1.stack.stack import Stack
import lab1.parse.prefix as prefix
import lab1.parse.parser as parser
import lab1.parse.validate as validate


def pre2post(expression: str) -> str:
    if not prefix.is_valid(expression):
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
        s = parsed_expression[index]
        if validate.is_parentheses(s):
            continue
        if validate.is_operation(str(s)):
            a = stack.pop()
            b = stack.pop()
            stack.push(f"{a}{b}{s}")
        elif isinstance(s, str):
            stack.push(s)
    while not stack.is_empty():
        s = stack.pop()
        postfix_expression_components.append(s)
    postfix_expression = "".join(postfix_expression_components)
    return postfix_expression
