import unittest
import lab2.convert.converter as converter
import lab2.convert.errors as errors
import lab2.parse.cleaner as cleaner


class TestPre2Post(unittest.TestCase):
    def test_converter_pre2post_raises_error_on_postfix_expression(self):
        with self.assertRaises(errors.InvalidExpressionError):
            converter.pre2post("AA+")

    def test_converter_pre2post_is_identity_for_single_element_prefix_expressions(self):
        prefix_expression = "A"
        postfix_expression = converter.pre2post(prefix_expression)
        self.assertEqual("A", postfix_expression)

    def test_converter_pre2post_is_identity_for_empty_prefix_expressions(self):
        prefix_expression = ""
        postfix_expression = converter.pre2post(prefix_expression)
        self.assertEqual("", postfix_expression)

    def test_converter_pre2post_raises_error_on_expression_with_too_many_operators(self):
        expression = "++AA"
        with self.assertRaises(errors.TooManyOperatorsError):
            converter._pre2post(
                expression=expression, segment=expression, node=None, depth=0, operators=0, operands=0)
        with self.assertRaises(errors.InvalidExpressionError):
            converter.pre2post(expression)

    def test_converter_pre2post_raises_error_on_expression_with_too_many_operands(self):
        expression = "++AAAA"
        with self.assertRaises(errors.TooManyOperandsError):
            converter._pre2post(
                expression=expression, segment=expression, node=None, depth=0, operators=0, operands=0)
        with self.assertRaises(errors.InvalidExpressionError):
            converter.pre2post(expression)

    def test_converter_pre2post_raises_error_on_prefix_expression_that_starts_with_operands(self):
        expression = "A+AB"
        with self.assertRaises(errors.InvalidExpressionError):
            converter._pre2post(
                expression=expression, segment=expression, node=None, depth=0, operators=0, operands=0)
        with self.assertRaises(errors.InvalidExpressionError):
            converter.pre2post(expression)

    def test_converter_pre2post_raises_error_on_prefix_expression_that_ends_with_an_operator(self):
        expression = "+ABB+"
        with self.assertRaises(errors.InvalidExpressionError):
            converter._pre2post(
                expression=expression, segment=expression, node=None, depth=0, operators=0, operands=0)
        with self.assertRaises(errors.InvalidExpressionError):
            converter.pre2post(expression)

    def test_converter_pre2post_raises_error_on_prefix_expression_with_illegal_characters(self):
        expression = "//A+B0-C+BA"
        with self.assertRaises(errors.IllegalOperandError):
            converter._pre2post(
                expression=expression, segment=expression, node=None, depth=0, operators=0, operands=0)
        with self.assertRaises(errors.InvalidExpressionError):
            converter.pre2post(expression)

    def test_converter_pre2post_converts_known_good_expressions_properly(self):
        self.assertEqual("AB+C-", converter.pre2post("-+ABC"))
        self.assertEqual("ABC+-", converter.pre2post("-A+BC"))
        self.assertEqual("AB-C+DEF-+$", converter.pre2post("$+-ABC+D-EF"))
        self.assertEqual("ABCDE-+$*EF*-", converter.pre2post("-*A$B+C-DE*EF"))
        self.assertEqual("ABC+*CBA-+*", converter.pre2post("**A+BC+C-BA"))
        self.assertEqual("ABC+$CBA-+*", converter.pre2post("*$A+BC+C-BA"))

    def test_converter_pre2post_converts_expressions_identically_with_and_without_whitespace(self):
        expression = "-+A BC      "
        clean_expression = cleaner.clean(expression)
        self.assertEqual(
            converter.pre2post(expression),
            converter.pre2post(clean_expression)
        )
