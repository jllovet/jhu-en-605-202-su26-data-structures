from lab1.stack.stack import Stack
import lab1.parse.parser as parser
import lab1.parse.validate as validate


def is_valid(expression: str) -> bool:
    # while input, read expression from left
    # if operand push onto stack
    # if operation
    #    pop A
    #    pop B
    #    perform operation // B op A
    #    push result
    try:
        parsed_expression = parser.parse(expression=expression, translate_symbols=True)
    except ValueError:
        return False
    if len(parsed_expression) == 1:
        return isinstance(parsed_expression[0], int)
    num_operations = 0
    num_operands = 0
    stack = Stack()
    parentheses_stack = Stack()
    for index in range(0, len(parsed_expression)):  # iterate from left
        s = parsed_expression[index]
        if validate.is_whitespace(s):
            return False
        if s == "(":
            parentheses_stack.push(s)
        if s == ")":
            if parentheses_stack.peek() == "(":
                _ = parentheses_stack.pop()
            else:
                return False  # unbalanced
        if isinstance(s, int):
            num_operands += 1
            stack.push(s)
        if validate.is_operation(str(s)):
            a = stack.pop()
            b = stack.pop()
            if not isinstance(a, int) or not isinstance(b, int):
                return False
            res = parser.execute_operation(s, a, b)  # type: ignore
            stack.push(res)
            num_operations += 1
    if stack.height == 1 and isinstance(stack.peek(), int):
        return True
    if not parentheses_stack.is_empty():
        return False
    if stack.is_empty() and num_operations == 0 and num_operands <= 1:
        return True
    if num_operations != (num_operands - 1):
        return False
    return True


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
