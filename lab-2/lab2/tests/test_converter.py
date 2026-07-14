import unittest
import lab2.convert.converter as converter
import lab2.convert.errors as errors


class TestPre2Post(unittest.TestCase):
    def test_converter_pre2post_raises_error_on_postfix_expression(self):
        with self.assertRaises(errors.InvalidExpressionError):
            print(converter.pre2post("AA+"))

    def test_converter_pre2post_is_identity_for_single_element_prefix_expressions(self):
        prefix_expression = "A"
        postfix_expression = converter.pre2post(prefix_expression)
        self.assertEqual("A", postfix_expression)

    def test_converter_pre2post_is_identity_for_empty_prefix_expressions(self):
        prefix_expression = ""
        postfix_expression = converter.pre2post(prefix_expression)
        self.assertEqual("", postfix_expression)
