import unittest
import lab1.stack as s
import lab1.parse.postfix as postfix
import lab1.parse.parser as parser


class TestIsValidPostfixExpression(unittest.TestCase):
    def test_is_valid_postfix_expression_returns_false_if_operand_to_operation_ratio_is_invalid(self):
        self.assertFalse(
            postfix.is_valid(parser.parse("AA++")))
        self.assertFalse(
            postfix.is_valid(parser.parse("A++")))
        self.assertFalse(
            postfix.is_valid(parser.parse("+")))

    def test_is_valid_postfix_expression_returns_true_if_operand_to_operation_ratio_is_valid(self):
        self.assertTrue(
            postfix.is_valid(parser.parse("AA+")))

    def test_is_valid_postfix_expression_returns_false_if_first_character_is_operation(self):
        self.assertFalse(
            postfix.is_valid(parser.parse("+AA")))

    def test_is_valid_postfix_expression_returns_true_for_empty_parentheses(self):
        self.assertTrue(
            postfix.is_valid(parser.parse("()")))

    def test_is_valid_postfix_expression_returns_false_for_unbalanced_parentheses(self):
        self.assertFalse(
            postfix.is_valid(parser.parse("(()")))
        self.assertFalse(
            postfix.is_valid(parser.parse("()(")))
        self.assertFalse(postfix.is_valid(
            parser.parse("()(()")))
    
    def test_is_valid_postfix_expression_returns_true_on_nested_postfix_expressions(self):
        self.assertTrue(postfix.is_valid(parser.parse("AB+C-")))
        self.assertTrue(postfix.is_valid(parser.parse("A(BC$)*((BC+)D-)+")))


class TestPostfixEvaluation(unittest.TestCase):
    def test_evaluate_postfix_returns_none_on_empty_string(self):
        expression = ""
        self.assertIsNone(postfix.evaluate(expression))

    def test_evaluate_postfix_returns_converted_symbol_on_unary_expression(self):
        self.assertEqual(1, postfix.evaluate("A"))
        self.assertEqual(2, postfix.evaluate("B"))
        self.assertEqual(26, postfix.evaluate("Z"))

    def test_evaluate_postfix_raises_error_for_multiple_operands_with_no_operation(self):
        with self.assertRaises(ValueError):
            postfix.evaluate("AB")
        with self.assertRaises(ValueError):
            postfix.evaluate("ABC")
        with self.assertRaises(ValueError):
            postfix.evaluate("ABCD")
    
    def test_evaluate_postfix_returns_evaluated_expression(self):
        self.assertEqual(2, postfix.evaluate("AA+"))
        self.assertEqual(3, postfix.evaluate("AB+"))
        self.assertEqual((1+2)*(3**4), postfix.evaluate("AB+(CD$)*"))

