from lab1.stack.stack import Stack
import lab1.parse.parser as parser
import lab1.parse.validate as validate


def is_valid(expression: str) -> bool:
    return validate.is_valid_expression(expression=expression, expression_type="prefix")


def evaluate(expression: str) -> int | None:
    # while input, read expression from right
    # if operand push onto stack
    # if operation
    #    pop A
    #    pop B
    #    perform operation // A op B
    #    push result
    if not is_valid(expression):
        raise ValueError(f"{expression} is not a valid prefix expression")
    parsed_expression = parser.parse(expression=expression, translate_symbols=True)
    if parsed_expression == []:
        return None
    stack = Stack()
    for i in range(0, len(parsed_expression)):  # iterate from right
        index = len(parsed_expression) - (i + 1)
        s = parsed_expression[index]
        if isinstance(s, int):
            stack.push(s)
        if validate.is_operator(str(s)):
            a = stack.pop()
            b = stack.pop()
            if not isinstance(a, int) or not isinstance(b, int):
                return False
            res = parser.execute_operation(s, a, b)  # type: ignore
            stack.push(res)
    if isinstance(stack.peek(), int):
        return stack.pop()  # type: ignore
    else:
        raise ValueError(f"Could not evaluate {expression}")
