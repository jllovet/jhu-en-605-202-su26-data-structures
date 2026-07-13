import unittest
import lab2.parse.parser as parser
import lab2.parse.cleaner as cleaner
import lab2.parse.evaluate as evaluate 


class TestClean(unittest.TestCase):
    def test_whitespace_is_stripped(self):
        self.assertNotIn(" ", cleaner.clean("AB+ "))
        self.assertNotIn(" ", cleaner.clean(" "))