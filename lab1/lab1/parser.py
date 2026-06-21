from lab1.stack import Stack


def lookup_symbol(symbol: str) -> int | str:
    if not symbol:
        return ""
    if ord(symbol) >= 65 and ord(symbol) <= 90:  # operands A - Z
        return ord(symbol) - 64
    else:
        return symbol


def parse(expression) -> list:
    parsed_symbols = []
    for s in expression:
        parsed_symbols.append(lookup_symbol(s))
    return parsed_symbols


def execute_operation(s: str, a: int, b: int) -> int:
    match s:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a // b
        case "$":
            return a ** b
    raise ValueError(
        f"Unable to execute operation {a}{s}{b}, because {s} was not recognized")


def is_valid_prefix_expression(parsed_expression: list) -> bool:
    # while input, read expression from right
    # if operand push onto stack
    # if operation
    #    pop A
    #    pop B
    #    perform operation // A op B
    #    push result
    if len(parsed_expression) == 1:
        return isinstance(parsed_expression[0], int)
    elif len(parsed_expression) > 1:
        if isinstance(parsed_expression[0], int):
            return False
    num_operations = 0
    num_operands = 0
    stack = Stack()
    parentheses_stack = Stack()
    for i in range(0, len(parsed_expression)):  # iterate from right
        index = len(parsed_expression) - (i + 1)
        s = parsed_expression[index]
        if s == ")":
            parentheses_stack.push(s)
        if s == "(":
            if parentheses_stack.peek() == ")":
                _ = parentheses_stack.pop()
            else:
                return False  # unbalanced
        if isinstance(s, int):
            num_operands += 1
            stack.push(s)
        if s == "+" or s == "-" or s == "/" or s == "*" or s == "$":
            a = stack.pop()
            b = stack.pop()
            if not isinstance(a, int) or not isinstance(b, int):
                return False
            res = execute_operation(s, a, b)  # type: ignore
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


def is_valid_postfix_expression(parsed_expression: list) -> bool:
    # while input, read expression from left
    # if operand push onto stack
    # if operation
    #    pop A
    #    pop B
    #    perform operation // B op A
    #    push result
    if len(parsed_expression) == 1:
        return isinstance(parsed_expression[0], int)
    num_operations = 0
    num_operands = 0
    stack = Stack()
    parentheses_stack = Stack()
    for index in range(0, len(parsed_expression)):  # iterate from left
        s = parsed_expression[index]
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
        if s == "+" or s == "-" or s == "/" or s == "*" or s == "$":
            a = stack.pop()
            b = stack.pop()
            if not isinstance(a, int) or not isinstance(b, int):
                return False
            res = execute_operation(s, a, b)  # type: ignore
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


def evaluate_postfix(expression: str) -> int | None:
    parsed_expression = parse(expression=expression)
    if parsed_expression == []:
        return None
    if not is_valid_prefix_expression(parsed_expression):
        raise ValueError(f"{expression} is not a valid prefix expression")
    return parsed_expression[0]
    # while input, read expression from left
    # if operand push onto stack
    # if operation
    #    pop A
    #    pop B
    #    perform operation // B op A
    #    push result


def evaluate_prefix(expression: str) -> int | None:
    parsed_expression = parse(expression=expression)
    if parsed_expression == []:
        return None
    if not is_valid_postfix_expression(parsed_expression):
        raise ValueError(f"{expression} is not a valid postfix expression")
    return parsed_expression[0]
    # while input, read expression from right
    # if operand push onto stack
    # if operation
    #    pop A
    #    pop B
    #    perform operation // A op B
    #    push result
