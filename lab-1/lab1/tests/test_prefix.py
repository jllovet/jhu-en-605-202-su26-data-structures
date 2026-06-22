import unittest
import lab1.parse.validate as validate
from lab1.parse.evaluate import eval


class TestIsValidPrefixExpression(unittest.TestCase):
    def test_is_valid_prefix_expression_returns_false_if_operand_to_operation_ratio_is_invalid(self):
        self.assertFalse(
            validate.is_valid_expression(expression="++AA", expression_type="prefix"))
        self.assertFalse(
            validate.is_valid_expression(expression="++A", expression_type="prefix"))
        self.assertFalse(
            validate.is_valid_expression(expression="+", expression_type="prefix"))

    def test_is_valid_prefix_expression_returns_false_if_expression_contains_whitespace(self):
        self.assertFalse(
            validate.is_valid_expression(expression="+AA ", expression_type="prefix"))
        self.assertFalse(
            validate.is_valid_expression(expression="+A A", expression_type="prefix"))
        self.assertFalse(
            validate.is_valid_expression(expression="+A  A ", expression_type="prefix"))

    def test_is_valid_prefix_expression_returns_true_if_operand_to_operation_ratio_is_valid(self):
        self.assertTrue(
            validate.is_valid_expression(expression="+AA", expression_type="prefix"))

    def test_is_valid_prefix_expression_returns_false_if_first_character_is_operand(self):
        self.assertFalse(
            validate.is_valid_expression(expression="AA+", expression_type="prefix"))
        self.assertFalse(
            validate.is_valid_expression(expression="A+A", expression_type="prefix"))

    def test_is_valid_prefix_expression_returns_true_for_empty_parentheses(self):
        self.assertTrue(
            validate.is_valid_expression(expression="()", expression_type="prefix"))

    def test_is_valid_prefix_expression_returns_false_for_unbalanced_parentheses(self):
        self.assertFalse(
            validate.is_valid_expression(expression="(()", expression_type="prefix"))
        self.assertFalse(
            validate.is_valid_expression(expression="()(", expression_type="prefix"))
        self.assertFalse(validate.is_valid_expression(
            expression="()(()", expression_type="prefix"))

    def test_is_valid_prefix_expression_returns_true_on_nested_prefix_expressions(self):
        self.assertTrue(validate.is_valid_expression(
            expression="+(-AB)C", expression_type="prefix"))
        self.assertTrue(validate.is_valid_expression(
            expression="+-AB*CD", expression_type="prefix"))


class TestPrefixEvaluation(unittest.TestCase):
    def test_evaluate_prefix_returns_none_on_empty_string(self):
        expression = ""
        self.assertIsNone(eval(expression, expression_type="prefix"))

    def test_evaluate_prefix_returns_converted_symbol_on_unary_expression(self):
        self.assertEqual(1, eval("A", expression_type="prefix"))
        self.assertEqual(2, eval("B", expression_type="prefix"))
        self.assertEqual(26, eval("Z", expression_type="prefix"))

    def test_evaluate_prefix_returns_evaluated_expression(self):
        self.assertEqual(2, eval("+AA", expression_type="prefix"))
        self.assertEqual(3, eval("+AB", expression_type="prefix"))
        self.assertEqual(
            (1+2)*(3**4), eval("*+AB($CD)", expression_type="prefix"))

    def test_evaluate_prefix_raises_error_for_multiple_operands_with_no_operation(self):
        with self.assertRaises(ValueError):
            eval("AB", expression_type="prefix")
        with self.assertRaises(ValueError):
            eval("ABC", expression_type="prefix")
        with self.assertRaises(ValueError):
            eval("ABCD", expression_type="prefix")
