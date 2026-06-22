import unittest
import lab1.parse.parser as parser
import lab1.parse.validate as validate

class TestSymbolClassifiers(unittest.TestCase):
    def test_is_whitespace(self):
        self.assertTrue(validate.is_whitespace(" "))
        self.assertTrue(validate.is_whitespace("\t"))
        self.assertTrue(validate.is_whitespace("\n"))
        self.assertTrue(validate.is_whitespace("\v"))
        self.assertTrue(validate.is_whitespace("\f"))
        self.assertFalse(validate.is_whitespace("A"))
        self.assertFalse(validate.is_whitespace(1)) # type: ignore
    
    def test_is_operation(self):
        self.assertTrue(validate.is_operation("+"))
        self.assertTrue(validate.is_operation("-"))
        self.assertTrue(validate.is_operation("/"))
        self.assertTrue(validate.is_operation("*"))
        self.assertTrue(validate.is_operation("$"))
        self.assertFalse(validate.is_operation("A"))
        self.assertFalse(validate.is_operation(1)) # type: ignore
    
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

        self.assertTrue(validate.is_allowed("+"))
        self.assertTrue(validate.is_allowed("-"))
        self.assertTrue(validate.is_allowed("*"))
        self.assertTrue(validate.is_allowed("/"))
        self.assertTrue(validate.is_allowed("$"))
        self.assertTrue(validate.is_allowed("("))
        self.assertTrue(validate.is_allowed(")"))
        
        self.assertFalse(validate.is_allowed("!"))
        self.assertFalse(validate.is_allowed("a"))
        self.assertFalse(validate.is_allowed("<"))
        

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
