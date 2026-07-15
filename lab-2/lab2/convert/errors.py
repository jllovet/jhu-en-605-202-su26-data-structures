class InvalidExpressionError(ValueError):
    def __init__(self, msg: str):
        super().__init__(msg)


class TooManyOperatorsError(InvalidExpressionError):
    def __init__(self, msg: str="Too many operators provided in expression"):
        super().__init__(msg)


class TooManyOperandsError(InvalidExpressionError):
    def __init__(self, msg: str="Too many operands provided in expression"):
        super().__init__(msg)

class IllegalOperandError(InvalidExpressionError):
    def __init__(self, msg: str="Illegal operand provided in expression"):
        super().__init__(msg)
