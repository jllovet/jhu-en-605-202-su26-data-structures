import unittest
import lab3.huffman.encoding.normalize as normalize


class TestIteration(unittest.TestCase):
    def test_strip_non_alphabetic_char(self):
        self.assertEqual("", normalize.strip_non_alphabetic_char(""))
        self.assertEqual("", normalize.strip_non_alphabetic_char("."))
        self.assertEqual("", normalize.strip_non_alphabetic_char(","))
        self.assertEqual("", normalize.strip_non_alphabetic_char("?"))
        self.assertEqual("", normalize.strip_non_alphabetic_char("]"))
        self.assertEqual("", normalize.strip_non_alphabetic_char("["))
        self.assertEqual("", normalize.strip_non_alphabetic_char("!"))
        self.assertEqual("", normalize.strip_non_alphabetic_char("+"))
        self.assertEqual("", normalize.strip_non_alphabetic_char("-"))
        self.assertEqual("", normalize.strip_non_alphabetic_char("!"))

    def test_normalize(self):
        self.assertEqual("", normalize.normalize(None))  # type:ignore
        self.assertEqual("HELLO", normalize.normalize("Hello!"))
        self.assertEqual("HELLOTHISISATEST",
                         normalize.normalize("Hello! This is a Test."))
        self.assertEqual("TOBEORNOTTOBETHATISTHEQUESTION",
                         normalize.normalize("To be or not to be, that is the question."))
        self.assertEqual("BACONIPSUMDOLORAMETPARIATURSAUSAGEALIQUAKEVINFILETMIGNON",
                         normalize.normalize("Bacon ipsum dolor amet pariatur sausage aliqua kevin filet mignon"))
        self.assertEqual("WERFERTIGISTDEMISTNICHTSRECHTZUMACHENEINWERDENDERWIRDIMMERDANKBARSEIN",
                         normalize.normalize("Wer fertig ist, dem ist nichts recht zu machen, ein Werdender wird immer dankbar sein"))
        self.assertEqual("SALLYSELLSSEASHELLSBYTHESEASHORE",
                         normalize.normalize("Sally sells seashells by the seashore."))
        self.assertEqual('PETERPIPERPICKEDAPECKOFPICKLEDPEPPERSAPECKOFPICKLEDPEPPERSPETERPIPERPICKED',
                         normalize.normalize("Peter Piper picked a peck of pickled peppers a peck of pickled peppers Peter Piper picked."))
        self.assertEqual('HOUSTONTHEEAGLEHASLANDED',
                         normalize.normalize("Houston, the Eagle has landed."))
        self.assertEqual('ISTHATYOURFINALANSWER',
                         normalize.normalize("Is that your final answer?"))
