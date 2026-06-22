import unittest
import lab1.convert.converter as converter
import lab1.parse.validate as validate
from lab1.parse.evaluate import eval


class TestPre2Post(unittest.TestCase):
    def test_converter_pre2post_raises_error_on_postfix_expression(self):
        with self.assertRaises(ValueError):
            converter.pre2post("AA+")

    def test_converter_pre2post_is_identity_for_single_element_prefix_expressions(self):
        prefix_expression = "A"
        postfix_expression = converter.pre2post(prefix_expression)
        self.assertTrue(validate.is_valid_expression(
            postfix_expression, expression_type="postfix"))
        self.assertEqual("A", postfix_expression)

    def test_converter_pre2post_is_identity_for_empty_prefix_expressions(self):
        prefix_expression = ""
        postfix_expression = converter.pre2post(prefix_expression)
        self.assertTrue(validate.is_valid_expression(
            postfix_expression, expression_type="postfix"))
        self.assertEqual("", postfix_expression)

    def test_converter_pre2post_returns_valid_postfix_expression(self):
        prefix_expression = "+AB"
        postfix_expression = converter.pre2post(prefix_expression)
        self.assertTrue(validate.is_valid_expression(
            postfix_expression, expression_type="postfix"))
        self.assertEqual("AB+", postfix_expression)

    def test_converter_pre2post_returns_equivalent_expression(self):
        prefix_expression = "+AA"
        postfix_expression = converter.pre2post(prefix_expression)
        self.assertEqual(
            eval(prefix_expression, expression_type="prefix"),
            eval(postfix_expression, expression_type="postfix")
        )

    def test_converter_pre2post_is_correct_for_complex_expressions(self):
        prefix_expression = "-+ABC"
        self.assertTrue(validate.is_valid_expression(
            expression=prefix_expression, expression_type="prefix"))

        prefix_expression = "-A+BC"
        self.assertTrue(validate.is_valid_expression(
            expression=prefix_expression, expression_type="prefix"))

        prefix_expression = "$+-ABC+D-EF"
        self.assertTrue(validate.is_valid_expression(
            expression=prefix_expression, expression_type="prefix"))

        prefix_expression = "-*A$B+C-DE*EF"
        self.assertTrue(validate.is_valid_expression(
            expression=prefix_expression, expression_type="prefix"))

        prefix_expression = "**A+BC+C-BA"
        self.assertTrue(validate.is_valid_expression(
            expression=prefix_expression, expression_type="prefix"))

        prefix_expression = "/A+BC +C*BA  "
        self.assertFalse(validate.is_valid_expression(
            expression=prefix_expression, expression_type="prefix"))

        prefix_expression = "*-*-ABC+BA  "
        self.assertFalse(validate.is_valid_expression(
            expression=prefix_expression, expression_type="prefix"))

        prefix_expression = "/+/A-BC-BA  "
        self.assertFalse(validate.is_valid_expression(
            expression=prefix_expression, expression_type="prefix"))

        prefix_expression = "*$A+BC+C-BA "
        self.assertFalse(validate.is_valid_expression(
            expression=prefix_expression, expression_type="prefix"))

        prefix_expression = "//A+B0-C+BA"
        self.assertFalse(validate.is_valid_expression(
            expression=prefix_expression, expression_type="prefix"))

        prefix_expression = "*$A^BC+C-BA"
        self.assertFalse(validate.is_valid_expression(
            expression=prefix_expression, expression_type="prefix"))
