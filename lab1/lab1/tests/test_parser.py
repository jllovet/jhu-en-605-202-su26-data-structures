import unittest
import lab1.stack as s
import lab1.parser as parser


class TestParser(unittest.TestCase):
    def test_capital_ascii_letters_return_number_in_valid_range(self):
        self.assertLessEqual(1, parser.lookup_symbol("A"))  # type: ignore
        self.assertGreaterEqual(
            26, parser.lookup_symbol("A"))  # type: ignore
        self.assertLessEqual(1, parser.lookup_symbol("B"))  # type: ignore
        self.assertGreaterEqual(
            26, parser.lookup_symbol("B"))  # type: ignore
        self.assertLessEqual(1, parser.lookup_symbol("Y"))  # type: ignore
        self.assertGreaterEqual(
            26, parser.lookup_symbol("Y"))  # type: ignore
        self.assertLessEqual(1, parser.lookup_symbol("Z"))  # type: ignore
        self.assertGreaterEqual(
            26, parser.lookup_symbol("Z"))  # type: ignore

    def test_other_symbols_returned_without_modification(self):
        self.assertEqual("", parser.lookup_symbol(""))
        self.assertEqual("+", parser.lookup_symbol("+"))
        self.assertEqual("-", parser.lookup_symbol("-"))
        self.assertEqual("*", parser.lookup_symbol("*"))
        self.assertEqual("/", parser.lookup_symbol("/"))
        self.assertEqual("$", parser.lookup_symbol("$"))
        self.assertEqual(")", parser.lookup_symbol(")"))
        self.assertEqual("(", parser.lookup_symbol("("))

    def test_parse_on_empty_expression_returns_empty_list(self):
        self.assertListEqual([], parser.parse(""))

    def test_parse_on_expression_with_operand_converts_them_to_singleton_list_of_ints(self):
        self.assertListEqual([1], parser.parse("A"))
        self.assertListEqual([26], parser.parse("Z"))

    def test_parse_on_expression_with_operands_converts_elements_to_ints(self):
        self.assertListEqual([1, 2, 3], parser.parse("ABC"))

    def test_parse_on_expression_with_operations_passes_transparently_to_list(self):
        self.assertListEqual(["(", ")"], parser.parse("()"))
        self.assertListEqual(["(", "+"], parser.parse("(+"))
        self.assertListEqual(["(", "/", "$"], parser.parse("(/$"))
        self.assertListEqual(["+"], parser.parse("+"))
        self.assertListEqual(["(", "+"], parser.parse("(+"))


class TestIsValidPrefixExpression(unittest.TestCase):
    def test_is_valid_prefix_expression_returns_false_if_operand_to_operation_ratio_is_invalid(self):
        self.assertFalse(
            parser.is_valid_prefix_expression(parser.parse("++AA")))
        self.assertFalse(
            parser.is_valid_prefix_expression(parser.parse("++A")))
        self.assertFalse(
            parser.is_valid_prefix_expression(parser.parse("+")))

    def test_is_valid_prefix_expression_returns_true_if_operand_to_operation_ratio_is_valid(self):
        self.assertTrue(
            parser.is_valid_prefix_expression(parser.parse("+AA")))

    def test_is_valid_prefix_expression_returns_false_if_first_character_is_operand(self):
        self.assertFalse(
            parser.is_valid_prefix_expression(parser.parse("AA+")))
        self.assertFalse(
            parser.is_valid_prefix_expression(parser.parse("A+A")))

    def test_is_valid_prefix_expression_returns_true_for_empty_parentheses(self):
        self.assertTrue(
            parser.is_valid_prefix_expression(parser.parse("()")))

    def test_is_valid_prefix_expression_returns_false_for_unbalanced_parentheses(self):
        self.assertFalse(
            parser.is_valid_prefix_expression(parser.parse("(()")))
        self.assertFalse(
            parser.is_valid_prefix_expression(parser.parse("()(")))
        self.assertFalse(parser.is_valid_prefix_expression(
            parser.parse("()(()")))


class TestIsValidPostfixExpression(unittest.TestCase):
    def test_is_valid_postfix_expression_returns_false_if_operand_to_operation_ratio_is_invalid(self):
        self.assertFalse(
            parser.is_valid_postfix_expression(parser.parse("AA++")))
        self.assertFalse(
            parser.is_valid_postfix_expression(parser.parse("A++")))
        self.assertFalse(
            parser.is_valid_postfix_expression(parser.parse("+")))

    def test_is_valid_postfix_expression_returns_true_if_operand_to_operation_ratio_is_valid(self):
        self.assertTrue(
            parser.is_valid_postfix_expression(parser.parse("AA+")))

    def test_is_valid_postfix_expression_returns_false_if_first_character_is_operation(self):
        self.assertFalse(
            parser.is_valid_postfix_expression(parser.parse("+AA")))

    def test_is_valid_postfix_expression_returns_true_for_empty_parentheses(self):
        self.assertTrue(
            parser.is_valid_postfix_expression(parser.parse("()")))

    def test_is_valid_postfix_expression_returns_false_for_unbalanced_parentheses(self):
        self.assertFalse(
            parser.is_valid_postfix_expression(parser.parse("(()")))
        self.assertFalse(
            parser.is_valid_postfix_expression(parser.parse("()(")))
        self.assertFalse(parser.is_valid_postfix_expression(
            parser.parse("()(()")))


class TestExecuteOperation(unittest.TestCase):
    def test_execute_operation_addition(self):
        self.assertEqual(1, parser.execute_operation("+", 1, 0))
        self.assertEqual(1, parser.execute_operation("+", 0, 1))
        self.assertEqual(2, parser.execute_operation("+", 1, 1))
        self.assertEqual(27, parser.execute_operation("+", 26, 1))

    def test_execute_operation_subtraction(self):
        self.assertEqual(1, parser.execute_operation("-", 1, 0))
        self.assertEqual(0, parser.execute_operation("-", 0, 0))
        self.assertEqual(-1, parser.execute_operation("-", 0, 1))

    def test_execute_operation_multiplication(self):
        self.assertEqual(0, parser.execute_operation("*", 1, 0))
        self.assertEqual(2, parser.execute_operation("*", 1, 2))
        self.assertEqual(52, parser.execute_operation("*", 26, 2))

    def test_execute_operation_integer_division(self):
        self.assertEqual(1, parser.execute_operation("/", 1, 1))
        self.assertEqual(-1, parser.execute_operation("/", 1, -1))
        self.assertEqual(1, parser.execute_operation("/", 2, 2))
        self.assertEqual(4, parser.execute_operation("/", 9, 2))
        with self.assertRaises(ZeroDivisionError):
            parser.execute_operation("/", 1, 0)

    def test_execute_operation_exponentiation(self):
        self.assertEqual(1, parser.execute_operation("$", 0, 0))
        self.assertEqual(0, parser.execute_operation("$", 0, 1))
        self.assertEqual(0, parser.execute_operation("$", 0, 2))
        self.assertEqual(1, parser.execute_operation("$", 1, 0))
        self.assertEqual(1, parser.execute_operation("$", 2, 0))
        self.assertEqual(1, parser.execute_operation("$", 1, 2))
        self.assertEqual(4, parser.execute_operation("$", 2, 2))
        self.assertEqual(16, parser.execute_operation("$", 4, 2))


class TestPostfixEvaluation(unittest.TestCase):
    def test_evaluate_postfix_returns_none_on_empty_string(self):
        expression = ""
        self.assertIsNone(parser.evaluate_postfix(expression))

    def test_evaluate_postfix_returns_converted_symbol_on_unary_expression(self):
        self.assertEqual(1, parser.evaluate_postfix("A"))
        self.assertEqual(2, parser.evaluate_postfix("B"))
        self.assertEqual(26, parser.evaluate_postfix("Z"))

    def test_evaluate_postfix_raises_error_for_multiple_operands_with_no_operation(self):
        with self.assertRaises(ValueError):
            parser.evaluate_postfix("AB")
        with self.assertRaises(ValueError):
            parser.evaluate_postfix("ABC")
        with self.assertRaises(ValueError):
            parser.evaluate_postfix("ABCD")


class TestPrefixEvaluation(unittest.TestCase):
    def test_evaluate_prefix_returns_none_on_empty_string(self):
        expression = ""
        self.assertIsNone(parser.evaluate_prefix(expression))

    def test_evaluate_prefix_returns_converted_symbol_on_unary_expression(self):
        self.assertEqual(1, parser.evaluate_prefix("A"))
        self.assertEqual(2, parser.evaluate_prefix("B"))
        self.assertEqual(26, parser.evaluate_prefix("Z"))

    def test_evaluate_prefix_raises_error_for_multiple_operands_with_no_operation(self):
        with self.assertRaises(ValueError):
            parser.evaluate_prefix("AB")
        with self.assertRaises(ValueError):
            parser.evaluate_prefix("ABC")
        with self.assertRaises(ValueError):
            parser.evaluate_prefix("ABCD")
