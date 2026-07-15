import lab2.convert.errors as errors
import lab2.parse.validate as validate
from typing import Optional


class Node:
    def __init__(self, parent, data, left=None, right=None):
        self.parent: Node | None = parent
        self.data: str = data
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def __str__(self, level=1):
        return f"{self.data}\n{'\t'*level}left: {self.left}\n{'\t'*level}right: {self.right}"

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
