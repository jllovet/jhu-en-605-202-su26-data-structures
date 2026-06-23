import unittest
import lab1.parse.parser as parser


class TestSymbolLookup(unittest.TestCase):
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


class TestParser(unittest.TestCase):
    def test_parser_does_not_convert_symbols_by_default(self):
        self.assertListEqual(["A"], parser.parse("A"))
        self.assertListEqual(["A"], parser.parse("A", translate_symbols=False))

    def test_parser_does_convert_symbols_if_flag_is_set(self):
        self.assertListEqual([1], parser.parse("A", translate_symbols=True))

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
        self.assertListEqual([1], parser.parse("A", translate_symbols=True))
        self.assertListEqual([26], parser.parse("Z", translate_symbols=True))

    def test_parse_on_expression_with_operands_converts_elements_to_ints(self):
        self.assertListEqual([1, 2, 3], parser.parse(
            "ABC", translate_symbols=True))

    def test_parse_on_expression_with_operations_passes_transparently_to_list(self):
        self.assertListEqual(["(", ")"], parser.parse("()"))
        self.assertListEqual(["(", "+"], parser.parse("(+"))
        self.assertListEqual(["(", "/", "$"], parser.parse("(/$"))
        self.assertListEqual(["+"], parser.parse("+"))
        self.assertListEqual(["(", "+"], parser.parse("(+"))

    def test_literal_integers_are_rejected(self):
        with self.assertRaises(ValueError):
            parser.parse("+A  A ")


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
