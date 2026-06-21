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
