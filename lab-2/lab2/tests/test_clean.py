import unittest
import lab2.parse.cleaner as cleaner


class TestClean(unittest.TestCase):
    def test_single_whitespace_is_stripped(self):
        self.assertNotIn(" ", cleaner.clean(" "))
        self.assertNotIn("\t", cleaner.clean("\t"))
        self.assertNotIn("\n", cleaner.clean("\n"))
        self.assertNotIn("\v", cleaner.clean("\v"))
        self.assertNotIn("\f", cleaner.clean("\f"))

        self.assertEqual("", cleaner.clean(" "))
        self.assertEqual("", cleaner.clean("\t"))
        self.assertEqual("", cleaner.clean("\n"))
        self.assertEqual("", cleaner.clean("\v"))
        self.assertEqual("", cleaner.clean("\f"))

    def test_single_suffix_whitespace_is_stripped(self):
        self.assertNotIn(" ", cleaner.clean("AB+ "))
        self.assertNotIn("\t", cleaner.clean("AB+\t"))
        self.assertNotIn("\n", cleaner.clean("AB+\n"))
        self.assertNotIn("\v", cleaner.clean("AB+\v"))
        self.assertNotIn("\f", cleaner.clean("AB+\f"))

        self.assertEqual("AB+", cleaner.clean("AB+ "))
        self.assertEqual("AB+", cleaner.clean("AB+\t"))
        self.assertEqual("AB+", cleaner.clean("AB+\n"))
        self.assertEqual("AB+", cleaner.clean("AB+\v"))
        self.assertEqual("AB+", cleaner.clean("AB+\f"))

    def test_single_prefix_whitespace_is_stripped(self):
        self.assertNotIn(" ", cleaner.clean(" AB+"))
        self.assertNotIn("\t", cleaner.clean("\tAB+"))
        self.assertNotIn("\n", cleaner.clean("\nAB+"))
        self.assertNotIn("\v", cleaner.clean("\vAB+"))
        self.assertNotIn("\f", cleaner.clean("\fAB+"))

        self.assertEqual("AB+", cleaner.clean(" AB+"))
        self.assertEqual("AB+", cleaner.clean("\tAB+"))
        self.assertEqual("AB+", cleaner.clean("\nAB+"))
        self.assertEqual("AB+", cleaner.clean("\vAB+"))
        self.assertEqual("AB+", cleaner.clean("\fAB+"))

    def test_single_infix_whitespace_is_stripped(self):
        self.assertNotIn(" ", cleaner.clean("A B+"))
        self.assertNotIn("\t", cleaner.clean("A\tB+"))
        self.assertNotIn("\n", cleaner.clean("A\nB+"))
        self.assertNotIn("\v", cleaner.clean("A\vB+"))
        self.assertNotIn("\f", cleaner.clean("A\fB+"))

        self.assertEqual("AB+", cleaner.clean("A B+"))
        self.assertEqual("AB+", cleaner.clean("A\tB+"))
        self.assertEqual("AB+", cleaner.clean("A\nB+"))
        self.assertEqual("AB+", cleaner.clean("A\vB+"))
        self.assertEqual("AB+", cleaner.clean("A\fB+"))

    def test_multiple_whitespace_is_stripped(self):
        self.assertNotIn(" ", cleaner.clean("  "))
        self.assertNotIn("\t", cleaner.clean("\t\t"))
        self.assertNotIn("\n", cleaner.clean("\n\n"))
        self.assertNotIn("\v", cleaner.clean("\v\v"))
        self.assertNotIn("\f", cleaner.clean("\f\f"))

        self.assertEqual("", cleaner.clean(" \t"))
        self.assertEqual("", cleaner.clean("\t\n"))
        self.assertEqual("", cleaner.clean("\n"))
        self.assertEqual("", cleaner.clean("\v "))
        self.assertEqual("", cleaner.clean("\f\n"))

    def test_multiple_suffix_whitespace_is_stripped(self):
        self.assertNotIn(" ", cleaner.clean("AB+  "))
        self.assertNotIn("\t", cleaner.clean("AB+\n\t"))
        self.assertNotIn("\n", cleaner.clean("AB+\t\n"))
        self.assertNotIn("\v", cleaner.clean("AB+\f\v"))
        self.assertNotIn("\f", cleaner.clean("AB+\f\n\t"))

        self.assertEqual("AB+", cleaner.clean("AB+  "))
        self.assertEqual("AB+", cleaner.clean("AB+\t\t\t\t"))
        self.assertEqual("AB+", cleaner.clean("AB+\n\t\n"))
        self.assertEqual("AB+", cleaner.clean("AB+\v\n"))
        self.assertEqual("AB+", cleaner.clean("AB+\f\f\f\t"))

    def test_multiple_prefix_whitespace_is_stripped(self):
        self.assertNotIn(" ",  cleaner.clean(" \t \nAB+"))
        self.assertNotIn("\t", cleaner.clean("\t\t\nAB+"))
        self.assertNotIn("\n", cleaner.clean("\n\n\nAB+"))
        self.assertNotIn("\v", cleaner.clean("\v\v\nAB+"))
        self.assertNotIn("\f", cleaner.clean("\f\f\nAB+"))

        self.assertEqual("AB+", cleaner.clean(" \t \nAB+"))
        self.assertEqual("AB+", cleaner.clean("\t\t\nAB+"))
        self.assertEqual("AB+", cleaner.clean("\n\n\nAB+"))
        self.assertEqual("AB+", cleaner.clean("\v\v\nAB+"))
        self.assertEqual("AB+", cleaner.clean("\f\f\nAB+"))

    def test_multiple_infix_whitespace_is_stripped(self):
        self.assertNotIn(" ",  cleaner.clean("A     \t  B+"))
        self.assertNotIn("\t", cleaner.clean("A\t\t\t\tB+"))
        self.assertNotIn("\n", cleaner.clean("A\n\n\n\nB+"))
        self.assertNotIn("\v", cleaner.clean("A\v\v\v\vB+"))
        self.assertNotIn("\f", cleaner.clean("A\f\f\f\fB+"))

        self.assertEqual("AB+", cleaner.clean("A     B+"))
        self.assertEqual("AB+", cleaner.clean("A\t\nB+"))
        self.assertEqual("AB+", cleaner.clean("A\n\v\fB+"))
        self.assertEqual("AB+", cleaner.clean("A\v\n \tB+"))
        self.assertEqual("AB+", cleaner.clean("A\f\vB+"))
