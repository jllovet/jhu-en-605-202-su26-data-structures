import unittest
import lab1.stack as s
import lab1.converter.converter as converter
import lab1.parse.postfix as postfix
import lab1.parse.prefix as prefix
import lab1.parse.parser as parser

class TestPre2Post(unittest.TestCase):
    def test_converter_pre2post_raises_error_on_postfix_expression(self):
        with self.assertRaises(ValueError):
            converter.pre2post("AA+")
    
    def test_converter_pre2post_is_identity_for_single_element_prefix_expressions(self):
        prefix_expression = "A"
        postfix_expression = converter.pre2post(prefix_expression)
        print(postfix_expression)
        self.assertTrue(postfix.is_valid(parser.parse(postfix_expression, translate_symbols=True)))
        self.assertEqual("A", postfix_expression)
        
    def test_converter_pre2post_is_identity_for_empty_prefix_expressions(self):
        prefix_expression = ""
        postfix_expression = converter.pre2post(prefix_expression)
        print(postfix_expression)
        self.assertTrue(postfix.is_valid(parser.parse(postfix_expression)))
        self.assertEqual("", postfix_expression)

    def test_converter_pre2post_returns_valid_postfix_expression(self):
        prefix_expression = "+AB"
        postfix_expression = converter.pre2post(prefix_expression)
        print(postfix_expression)
        self.assertTrue(postfix.is_valid(parser.parse(postfix_expression, translate_symbols=True)))
        self.assertEqual("AB+", postfix_expression)

    def test_converter_pre2post_returns_equivalent_expression(self):
        prefix_expression = "+AA"
        postfix_expression = converter.pre2post(prefix_expression)
        self.assertEqual(
            prefix.evaluate(prefix_expression),
            postfix.evaluate(postfix_expression)
        )

