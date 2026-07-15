class InvalidExpressionError(ValueError):
    """Custom Error type that inherits from ValueError

    Base type used for other custom Errors

    Args:
        msg: str a custom message for the error
    """

    def __init__(self, msg: str):
        super().__init__(msg)


class TooManyOperatorsError(InvalidExpressionError):
    """Custom Error type that inherits from InvalidExpressionError

    Indicates to the caller that there were too many operators in an expression

    Args:
        msg: str a custom message for the error
    """

    def __init__(self, msg: str = "Too many operators provided in expression"):
        super().__init__(msg)


class TooManyOperandsError(InvalidExpressionError):
    """Custom Error type that inherits from InvalidExpressionError

    Indicates to the caller that there were too many operands in an expression

    Args:
        msg: str a custom message for the error
    """

    def __init__(self, msg: str = "Too many operands provided in expression"):
        super().__init__(msg)


class IllegalOperandError(InvalidExpressionError):
    """Custom Error type that inherits from InvalidExpressionError

    Indicates to the caller that there was an illegal operator in an expression

    Args:
        msg: str a custom message for the error
    """

    def __init__(self, msg: str = "Illegal operand provided in expression"):
        super().__init__(msg)
