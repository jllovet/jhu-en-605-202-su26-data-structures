import lab2.convert.errors as errors
import lab2.internal.parse.validate as validate
from lab2.internal.tree.tree import Node
from typing import Tuple
import logging
logger = logging.getLogger(__name__)


def is_skip_char(s: str) -> bool:
    """Returns bool indicating whether character can be skipped

    Args:
        s: str to evaluate whether it should be skipped

    Returns:
        bool indicating whether character can be skipped

    Raises:
        None

    Side Effects:
        None

    Idempotent:
        True
    """
    return s.isspace() or validate.is_parenthesis(s)


def skip(expression: str, segment: str) -> Tuple[str, str, bool]:
    """Skips over irrelevant characters up to the next relevant or end of expression

    Args:
        expression: str the original expression
        segment: str the segment possibly containing irrelevant characters as prefix

    Returns:
        str: new segment
        str: current char at the beginning of the new segment
        bool: indicating whether the new segment segment is the last segment

    Raises:
        None

    Side Effects:
        Writes to logs

    Idempotent:
        True
    """
    logging.debug(f"Skipping whitespace, non-operands, and non-operators")
    index = len(expression) - len(segment)
    is_last_segment = index == len(expression) - 1
    current_char = expression[index]
    while is_skip_char(current_char) and not is_last_segment:  # silently step past
        logging.debug(f"CURRENT CHAR:'{current_char}'")
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
    # Raise error if the expression starts with an operand
    if depth == 0 and len(expression) > 1 and validate.is_operand(expression[0]):
        msg = f"'{expression}' could not be processed. Prefix expressions can't start with an operand."
        logger.error(msg)
        raise errors.InvalidExpressionError(msg=msg)

    index = len(expression) - len(segment)
    is_last_segment = index == len(expression) - 1
    current_char = expression[index]

    # Raise error if there are illegal characters
    if not any([validate.is_operand(current_char), validate.is_operator(current_char), is_skip_char(current_char)]):
        msg=f"'{expression}' has an illegal character '{current_char}' at position {index+1}."
        logger.error(msg)
        raise errors.IllegalOperandError(msg)

    # We need to skip whitespace and irrelevant characters we encounter
    logging.debug(f"Considering whether to skip characters")
    logging.debug(f"CURRENT: '{current_char}'")
    if is_skip_char(current_char):  # silently step past
        segment, current_char, is_last_segment = skip(
            expression=expression,
            segment=segment)

    # One more special scenario, in case we have already reached the last segment of the expression
    if is_last_segment:
        # Raise an error if the expression ends with an operator
        if validate.is_operator(current_char):
            msg=f"'{expression}' could not be processed. Prefix expressions cannot end with an operator."
            logger.error(msg)
            raise errors.TooManyOperatorsError(msg)
        # A node should not be created if we encounter an irrelevant character
        if is_skip_char(current_char):
            n = None
        else:  # But a node should be created if we encounter a relevant character!
            logging.debug(f"MAKING NODE FROM:'{current_char}'")
            n = Node(parent=node, data=current_char, left=None, right=None)
        return expression, \
            segment, \
            n, \
            depth-1, \
            operators, \
            operands + 1 if validate.is_operand(current_char) else operands

    logging.debug(f"CURRENT CHAR:{current_char}")
    logging.debug(f"MAKING NODE FROM:'{current_char}'")
    n = Node(parent=node, data=current_char, left=None, right=None)
    try:
        # Handle operator
        if validate.is_operator(current_char):
            logging.debug(f"FOUND OPERATOR:{current_char}")
            operators += 1
            # This horrible formatting is because of how many arguments and return values we have
            # LEFT CHILD
            expression, segment, \
                left, depth, \
                operators, operands = _pre2post(expression=expression,
                                                segment=segment[1:],
                                                node=n,
                                                depth=depth+1,
                                                operators=operators,
                                                operands=operands)

            n.left = left if left else None
            # RIGHT CHILD
            expression, segment, \
                right, depth, \
                operators, operands = _pre2post(expression=expression,
                                                segment=segment[1:],
                                                node=n,
                                                depth=depth+1,
                                                operators=operators,
                                                operands=operands)
            n.right = right if right else None
        # Handle operand: Note that this should not recurse, since the operands must be leaves
        if validate.is_operand(current_char):
            operands += 1

    # Index error can occur in the recursion above if the expression is not balanced
    except IndexError:
        # Return a specific error if we can
        if operands <= operators:
            msg=f"'{expression}' has too many operators."
            logger.error(msg)
            raise errors.TooManyOperatorsError(msg)
        else:  # Otherwise fall back to a generic one
            msg=f"'{expression}' could not be processed. Please ensure it has a valid prefix structure."
            logger.error(msg)
            raise errors.InvalidExpressionError(msg)

    if depth != 0:
        return expression, segment, n, depth-1, operators, operands

    # Now we are back to the top of the tree, and we should be finished with recursive calls
    # But we need to do some housekeeping checks before we can return
    index = len(expression) - len(segment)
    is_last_segment = index == len(expression) - 1
    logging.debug(f"AT DEPTH 0: OPERATORS:{operators} OPERANDS:{operands}")
    # If we're not at the end of the string, we're going to scan ahead to see whether there's anything relevant left
    if not is_last_segment:
        segment = segment[1:]
        index = len(expression) - len(segment)
        current_char = expression[index]
        if is_skip_char(current_char):  # silently step past
            logging.debug(f"AT DEPTH 0: SKIPPING UNNEEDED CHARACTERS")
            segment, current_char, is_last_segment = skip(
                expression=expression,
                segment=segment)
        else:  # We found something relevant when we shouldn't have, meaning the expression is ill-structured
            msg=f"'{expression}' has too many operands."
            logger.error(msg)
            raise errors.TooManyOperandsError(msg)

    # Since we may skipped over irrelevant characters, we have to recalculate in case state was changed above
    index = len(expression) - len(segment)
    is_last_segment = index == len(expression) - 1

    # If we get here, there was an issue with the conversion, and the expression is likely ill-structured
    if not is_last_segment:
        msg=f"'{expression}' could not be processed. Please ensure it has a valid prefix structure."
        logger.error(msg)
        raise errors.InvalidExpressionError(msg)

    # Check for operand-operator balance
    # Happy path
    if operands - operators == 1:
        return expression, segment, n, depth-1, operators, operands
    # Unbalanced
    elif operands <= operators:
        msg=f"'{expression}' has too many operators."
        logger.error(msg)
        raise errors.TooManyOperatorsError(msg)
    # Unbalanced
    elif operands > operators:
        msg=f"'{expression}' has too many operators."
        logger.error(msg)
        raise errors.TooManyOperandsError(msg)

    # If we have cleared all the checks above, we can return
    return expression, segment, n, depth-1, operators, operands


def tree2str(tree) -> str:
    if tree:
        return "".join(n for n in tree)
    else:
        return ""


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
        InvalidExpressionError: if the expression is not a valid prefix expression

    Side Effects:
        Raises InvalidExpressionError if the expression provided was not valid
        Writes to logs

    Idempotent:
        True
    """
    logger.info(f"Attempting to convert: '{expression}'")
    try:
        _, _, tree, _, operators, operands = _pre2post(
            expression=expression, segment=expression, node=None, depth=0, operators=0, operands=0)
        if operands == 0 and operators == 0:
            return ""
        postfix = tree2str(tree)
        logger.debug(f"POSTFIX EXPRESSION: '{postfix}'")
        return postfix
    except (errors.InvalidExpressionError) as err:
        logger.error(f"Reraising error: {err}")
        raise errors.InvalidExpressionError(
            f"{err}")
    finally:
        pass
