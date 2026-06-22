import unittest
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
    
    def test_is_parentheses(self):
        self.assertTrue(validate.is_parentheses("("))
        self.assertTrue(validate.is_parentheses(")"))
        self.assertFalse(validate.is_parentheses("A"))
        self.assertFalse(validate.is_parentheses("+"))
        self.assertFalse(validate.is_parentheses(1)) # type: ignore

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
        self.assertFalse(validate.is_allowed(1)) # type: ignore
        
