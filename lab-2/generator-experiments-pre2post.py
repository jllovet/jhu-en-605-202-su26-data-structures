from typing import Tuple, Optional
import lab2.convert.errors as errors
import lab2.parse.validate as validate


def is_operand(symbol: str) -> bool:
    """Returns a boolean indicating whether the symbol is an operand

    Returns true when symbol.islpha() is True

    Args:
        symbol: str a single character from an expression

    Returns:
        A bool indicating whether the symbol is an operand

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        True
    """
    if not isinstance(symbol, str):
        return False
    return symbol.isalpha()


def is_operator(symbol: str) -> bool:
    """Returns a boolean indicating whether the symbol is an operator

    Returns true if the symbol is in one of the operators: +, -, *, /, $

    Args:
        symbol: str a single character from an expression

    Returns:
        A bool indicating whether the symbol is an operator

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        True
    """
    if not isinstance(symbol, str):
        return False
    match symbol:
        case "+":
            return True
        case "-":
            return True
        case "/":
            return True
        case "*":
            return True
        case "$":
            return True
    return False


def is_operator_or_bracket(symbol: str) -> bool:
    """Returns a boolean indicating whether the symbol is an operator or parenthesis

    Returns true if the symbol is any of +, -, *, /, $, (, )

    Args:
        symbol: str a single character from an expression

    Returns:
        A bool indicating whether the symbol is any of +, -, *, /, $, (, )

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        True
    """
    if not isinstance(symbol, str):
        return False
    return (symbol in ["+", "-", "*", "/", "$", "(", ")"])


def is_parenthesis(symbol: str) -> bool:
    """Returns a boolean indicating whether the symbol is "(" or ")"

    Args:
        symbol: str a single character from an expression

    Returns:
        A bool indicating whether the symbol is a parenthesis

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        True
    """
    return symbol == "(" or symbol == ")"




class Node:
    def __init__(self, parent, data, left=None, right=None):
        self.parent: Node | None = parent
        self.data: str = data
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def __str__(self, level=1):
        return f"{self.data}\n{'\t'*level}left: {self.left}\n{'\t'*level}right: {self.right}"
        # return f"{self.data}, left: {self.left}, right: {self.right}"

    def __iter__(self):
        if self.left:
            yield from self.left
        if self.right:
            yield from self.right
        yield self.data

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def operator_is_leaf(self) -> bool:
        if validate.is_operand(self.data):
            return False
        if validate.is_operator(self.data) and self.is_leaf():
            return True
        return False

    def operand_has_operator_child(self) -> bool:
        if not validate.is_operand(self.data):
            return False
        if self.left and validate.is_operator(self.left.data):
            return True
        if self.right and validate.is_operator(self.right.data):
            return True
        return False

    def has_too_many_operators(self) -> bool:
        if self.operand_has_operator_child() or self.operator_is_leaf():
            return True
        return False

    def has_too_many_operands(self) -> bool:
        if validate.is_operand(self.data) and not self.is_leaf():
            return True
        return False

    def raise_errors_for_invalid_structure(self, expression):
        if self.has_too_many_operators():
            raise errors.TooManyOperatorsError(
                msg=f"In '{expression}' too many operators were provided")
        if self.has_too_many_operands():
            raise errors.TooManyOperandsError(
                msg=f"In '{expression}' too many operands were provided"
            )


def is_skip_char(s: str) -> bool:
    return s.isspace() or validate.is_parenthesis(s)


def skip(expression: str, segment: str) -> Tuple[str, str, bool]:
    index = len(expression) - len(segment)
    is_last_segment = index == len(expression) - 1
    current_char = expression[index]
    while is_skip_char(current_char) and not is_last_segment:  # silently step past
        # print(f"CURRENT CHAR:{current_char}")
        segment = segment[1:]
        index = len(expression) - len(segment)
        is_last_segment = index == len(expression) - 1
        current_char = expression[index]
    return segment, current_char, is_last_segment


def _pre2post(expression: str, segment: str, node: Node | None, depth: int, operators: int = 0, operands: int = 0) \
        -> Tuple[str, str, Node | None, int, int, int]:
    # Fail Fast
    if expression == "":
        return expression, segment, None, depth, operators, operands
    index = len(expression) - len(segment)
    is_last_segment = index == len(expression) - 1
    current_char = expression[index]
    if not any([validate.is_operand(current_char), validate.is_operator(current_char), is_skip_char(current_char)]):
        raise errors.IllegalOperandError(f"In '{expression}' the value '{current_char}' at position {index+1} is an illegal character")
    # print(f"CURRENT: '{current_char}'")
    if is_skip_char(current_char):  # silently step past
        segment, current_char, is_last_segment = skip(
            expression=expression,
            segment=segment)
    if is_last_segment:
        if validate.is_operator(current_char):
            raise errors.TooManyOperatorsError(
                "Cannot have operator in final position of a prefix expression")
        if is_skip_char(current_char):
            n = None
        else:
            # print(f"MAKING NODE FROM:'{current_char}'")
            n = Node(parent=node, data=current_char, left=None, right=None)
        return expression, \
            segment, \
            n, \
            depth-1, \
            operators, \
            operands + 1 if validate.is_operand(current_char) else operands
    # print(f"MAKING NODE FROM:'{current_char}'")
    n = Node(parent=node, data=current_char, left=None, right=None)
    # operator
    # print(f"CURRENT CHAR:{current_char}")
    if validate.is_operator(current_char):
        # print(f"FOUND OPERATOR:{current_char}")
        operators += 1
        expression, segment, left, depth, operators, operands = _pre2post(expression=expression,
                                                                          segment=segment[1:],
                                                                          node=n,
                                                                          depth=depth+1,
                                                                          operators=operators,
                                                                          operands=operands)

        n.left = left if left else None
        expression, segment, right, depth, operators, operands = _pre2post(expression=expression,
                                                                           segment=segment[1:],
                                                                           node=n,
                                                                           depth=depth+1,
                                                                           operators=operators,
                                                                           operands=operands)
        n.right = right if right else None
    # operand
    if validate.is_operand(current_char):
        operands += 1
    # Back to the top of the tree, should be finished with recursive calls
    if depth == 0:
        index = len(expression) - len(segment)
        is_last_segment = index == len(expression) - 1
        # print(f"AT DEPTH 0: OPERATORS:{operators} OPERANDS:{operands}")
        if not is_last_segment:
            segment = segment[1:]
            if is_skip_char(current_char):  # silently step past
                # print(f"AT DEPTH 0: SKIPPING UNNEEDED CHARACTERS")
                segment, current_char, is_last_segment = skip(
                    expression=expression,
                    segment=segment)
            index = len(expression) - len(segment)
            is_last_segment = index == len(expression) - 1
        if not is_last_segment:
            raise errors.InvalidExpressionError(
                msg=f"In '{expression}' there were components that could not be processed. Please validate the structure of the prefix expression."
            )
        if operands - operators == 1:
            return expression, segment, n, depth-1, operators, operands
        elif operands <= operators:
            raise errors.TooManyOperatorsError(
                msg=f"In '{expression}' too many operators were provided.")
        elif operands > operators:
            raise errors.TooManyOperandsError(
                msg=f"In '{expression}' too many operands were provided.")
    return expression, segment, n, depth-1, operators, operands


def tree2str(tree) -> str:
    if tree:
        return "".join(n for n in tree)
    else:
        return ""


expressions = [
    '+AB',
    '-+ABC',
    '-A+BC',
    '$+-ABC+D-EF',
    '-*A$B+C-DE*EF',
    '**A+BC+C-BA',
    '/A+BC +C*BA  ',
    '*-*-ABC+BA  ',
    '/+/A-BC-BA  ',
    '*$A+BC+C-BA ',
    '//A+B0-C+BA',
    '*$A^BC+C-BA					',
    '  ()) (+AB)'
]

for expression in expressions:
    print(f"PROCESSING EXPRESSION:'{expression}'")
    try:
        _, _, tree, _, operators, operands = _pre2post(
            expression=expression, segment=expression, node=None, depth=0, operators=0, operands=0)
        print(f"POSTFIX EXPRESSION: '{tree2str(tree)}'")
    except (errors.InvalidExpressionError) as err:
        print("Couldn't process the expression! ", err)
    finally:
        print("-"*80)
