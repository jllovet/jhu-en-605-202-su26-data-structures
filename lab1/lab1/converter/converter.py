from lab1.stack import Stack
import lab1.parse.postfix as postfix
import lab1.parse.prefix as prefix
import lab1.parse.parser as parser


def pre2post(expression: str) -> str:
    if not prefix.is_valid(expression):
        raise ValueError(f"{expression} is not a valid prefix expression")
    stack = Stack()
    parentheses_stack = Stack()
    parsed_expression = parser.parse(expression=expression)
    postfix_expression_components = []
    if parsed_expression == [] or len(parsed_expression) == 1:
        return expression
    for i in range(0, len(parsed_expression)):  # iterate from right
        index = len(parsed_expression) - (i + 1)
        s = parsed_expression[index]
        if s == ")":
            parentheses_stack.push(s)
        if s == "(":
            # We don't need to check that top is ")",
            # because we already checked that this is a valid expression,
            # which implies that the parentheses are balanced.
            _ = parentheses_stack.pop()
        if s == "+" or s == "-" or s == "/" or s == "*" or s == "$":
            a = stack.pop()
            b = stack.pop()
            postfix_expression_components.append(a)
            postfix_expression_components.append(b)
            postfix_expression_components.append(s)
        elif isinstance(s, str):
            stack.push(s)
    while not stack.is_empty():
        s = stack.pop()
        postfix_expression_components.append(s)
    postfix_expression = "".join(postfix_expression_components)
    return postfix_expression
