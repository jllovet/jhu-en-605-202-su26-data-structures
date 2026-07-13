import unittest
import lab2.parse.validate as validate


class TestSymbolClassifiers(unittest.TestCase):
    def test_is_whitespace(self):
        self.assertTrue(validate.is_whitespace(" "))
        self.assertTrue(validate.is_whitespace("\t"))
        self.assertTrue(validate.is_whitespace("\n"))
        self.assertTrue(validate.is_whitespace("\v"))
        self.assertTrue(validate.is_whitespace("\f"))
        self.assertFalse(validate.is_whitespace("A"))
        self.assertFalse(validate.is_whitespace(1))  # type: ignore

    def test_is_parentheses(self):
        self.assertTrue(validate.is_parenthesis("("))
        self.assertTrue(validate.is_parenthesis(")"))
        self.assertFalse(validate.is_parenthesis("A"))
        self.assertFalse(validate.is_parenthesis("+"))
        self.assertFalse(validate.is_parenthesis(1))  # type: ignore

    def test_is_operation(self):
        self.assertTrue(validate.is_operator("+"))
        self.assertTrue(validate.is_operator("-"))
        self.assertTrue(validate.is_operator("/"))
        self.assertTrue(validate.is_operator("*"))
        self.assertTrue(validate.is_operator("$"))
        self.assertFalse(validate.is_operator("A"))
        self.assertFalse(validate.is_operator(1))  # type: ignore

    def test_is_allowed(self):
        self.assertTrue(validate.is_allowed("A"))
        self.assertTrue(validate.is_allowed("B"))
        self.assertTrue(validate.is_allowed("C"))
        self.assertTrue(validate.is_allowed("D"))
        self.assertTrue(validate.is_allowed("E"))
        self.assertTrue(validate.is_allowed("F"))
        self.assertTrue(validate.is_allowed("G"))
        self.assertTrue(validate.is_allowed("H"))
        self.assertTrue(validate.is_allowed("I"))
        self.assertTrue(validate.is_allowed("J"))
        self.assertTrue(validate.is_allowed("K"))
        self.assertTrue(validate.is_allowed("L"))
        self.assertTrue(validate.is_allowed("M"))
        self.assertTrue(validate.is_allowed("N"))
        self.assertTrue(validate.is_allowed("O"))
        self.assertTrue(validate.is_allowed("P"))
        self.assertTrue(validate.is_allowed("Q"))
        self.assertTrue(validate.is_allowed("R"))
        self.assertTrue(validate.is_allowed("S"))
        self.assertTrue(validate.is_allowed("T"))
        self.assertTrue(validate.is_allowed("U"))
        self.assertTrue(validate.is_allowed("V"))
        self.assertTrue(validate.is_allowed("W"))
        self.assertTrue(validate.is_allowed("X"))
        self.assertTrue(validate.is_allowed("Y"))
        self.assertTrue(validate.is_allowed("Z"))
        self.assertTrue(validate.is_allowed("a"))

        self.assertTrue(validate.is_allowed("+"))
        self.assertTrue(validate.is_allowed("-"))
        self.assertTrue(validate.is_allowed("*"))
        self.assertTrue(validate.is_allowed("/"))
        self.assertTrue(validate.is_allowed("$"))
        self.assertTrue(validate.is_allowed("("))
        self.assertTrue(validate.is_allowed(")"))

        self.assertFalse(validate.is_allowed("!"))
        self.assertFalse(validate.is_allowed("<"))
        self.assertFalse(validate.is_allowed(1))  # type: ignore


class TestIsValidExpression(unittest.TestCase):
    def is_valid_expression(self):
        self.assertTrue(validate.is_valid_expression("+AB", "prefix"))
        self.assertFalse(validate.is_valid_expression("+AB", "postfix"))
        self.assertTrue(validate.is_valid_expression("AB+", "postfix"))
        self.assertFalse(validate.is_valid_expression("AB+", "prefix"))


class TestExpressionInvariants(unittest.TestCase):
    def test_is_singleton_operand(self):
        self.assertTrue(validate.is_singleton_operand(["A"]))
        self.assertTrue(validate.is_singleton_operand([1]))
        self.assertFalse(validate.is_singleton_operand([]))
        self.assertFalse(validate.is_singleton_operand(["A", "A"]))
        self.assertFalse(validate.is_singleton_operand(["+", "A", "B"]))
        self.assertFalse(validate.is_singleton_operand(["+"]))

    def test_is_start_of_nontrivial_prefix_expression_an_operand(self):
        self.assertTrue(
            validate.is_start_of_expression_an_operand(["A", "+", "A", "A"]))
