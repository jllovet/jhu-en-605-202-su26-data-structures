from lab1.stack.stack import Stack
import lab1.parse.parser as parser
import lab1.parse.validate as validate


def is_valid(expression: str) -> bool:
    return validate.is_valid_expression(expression, expression_type="postfix")


def evaluate(expression: str) -> int | None:
    # while input, read expression from left
    # if operand push onto stack
    # if operation
    #    pop A
    #    pop B
    #    perform operation // B op A
    #    push result
    if not is_valid(expression):
        raise ValueError(f"{expression} is not a valid postfix expression")
    parsed_expression = parser.parse(expression=expression, translate_symbols=True)
    if parsed_expression == []:
        return None
    stack = Stack()
    for index in range(0, len(parsed_expression)):  # iterate from left
        s = parsed_expression[index]
        if isinstance(s, int):
            stack.push(s)
        if validate.is_operation(str(s)):
            b = stack.pop()
            a = stack.pop()
            if not isinstance(a, int) or not isinstance(b, int):
                return False
            res = parser.execute_operation(s, a, b)  # type: ignore
            stack.push(res)
    if isinstance(stack.peek(), int):
        return stack.pop()  # type: ignore
    else:
        raise ValueError(f"Could not evaluate {expression}")
