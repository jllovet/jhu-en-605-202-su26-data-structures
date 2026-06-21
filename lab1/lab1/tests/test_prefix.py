import unittest
import lab1.stack as s
import lab1.parse.prefix as prefix
import lab1.parse.parser as parser



class TestIsValidPrefixExpression(unittest.TestCase):
    def test_is_valid_prefix_expression_returns_false_if_operand_to_operation_ratio_is_invalid(self):
        self.assertFalse(
            prefix.is_valid(parser.parse("++AA")))
        self.assertFalse(
            prefix.is_valid(parser.parse("++A")))
        self.assertFalse(
            prefix.is_valid(parser.parse("+")))

    def test_is_valid_prefix_expression_returns_true_if_operand_to_operation_ratio_is_valid(self):
        self.assertTrue(
            prefix.is_valid(parser.parse("+AA", translate_symbols=True)))

    def test_is_valid_prefix_expression_returns_false_if_first_character_is_operand(self):
        self.assertFalse(
            prefix.is_valid(parser.parse("AA+")))
        self.assertFalse(
            prefix.is_valid(parser.parse("A+A")))

    def test_is_valid_prefix_expression_returns_true_for_empty_parentheses(self):
        self.assertTrue(
            prefix.is_valid(parser.parse("()")))

    def test_is_valid_prefix_expression_returns_false_for_unbalanced_parentheses(self):
        self.assertFalse(
            prefix.is_valid(parser.parse("(()")))
        self.assertFalse(
            prefix.is_valid(parser.parse("()(")))
        self.assertFalse(prefix.is_valid(
            parser.parse("()(()")))
    
    def test_is_valid_prefix_expression_returns_true_on_nested_prefix_expressions(self):
        self.assertTrue(prefix.is_valid(parser.parse("+(-AB)C", translate_symbols=True)))
        self.assertTrue(prefix.is_valid(parser.parse("+-AB*CD", translate_symbols=True)))


class TestPrefixEvaluation(unittest.TestCase):
    def test_evaluate_prefix_returns_none_on_empty_string(self):
        expression = ""
        self.assertIsNone(prefix.evaluate(expression))

    def test_evaluate_prefix_returns_converted_symbol_on_unary_expression(self):
        self.assertEqual(1, prefix.evaluate("A"))
        self.assertEqual(2, prefix.evaluate("B"))
        self.assertEqual(26, prefix.evaluate("Z"))
    
    def test_evaluate_prefix_returns_evaluated_expression(self):
        self.assertEqual(2, prefix.evaluate("+AA"))
        self.assertEqual(3, prefix.evaluate("+AB"))
        self.assertEqual((1+2)*(3**4), prefix.evaluate("*+AB($CD)"))

    def test_evaluate_prefix_raises_error_for_multiple_operands_with_no_operation(self):
        with self.assertRaises(ValueError):
            prefix.evaluate("AB")
        with self.assertRaises(ValueError):
            prefix.evaluate("ABC")
        with self.assertRaises(ValueError):
            prefix.evaluate("ABCD")
