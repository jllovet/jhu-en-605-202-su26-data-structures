import unittest
import lab3.huffman.encode as encode
from lab3.huffman.encode import EncodingData


class TestFrequencyListToEncodingData(unittest.TestCase):
    def test_single_element(self):
        mock_file = ["A - 1"]
        manual = [EncodingData(characters="A", score=1)]
        self.assertListEqual(manual, encode.frequency_to_encoding_data(mock_file))

    def test_unclean_data(self):
        mock_file = ["A - 1 "]
        manual = [EncodingData(characters="A", score=1)]
        self.assertListEqual(manual, encode.frequency_to_encoding_data(mock_file))

        mock_file = ["A - 1 2"]
        manual = [EncodingData(characters="A", score=12)]
        with self.assertRaises(ValueError):
            encode.frequency_to_encoding_data(mock_file)

        mock_file = ["A.B - 1B2"]
        manual = [EncodingData(characters="A", score=12)]
        with self.assertRaises(ValueError):
            encode.frequency_to_encoding_data(mock_file)

        mock_file = ["A.B - 1B2", "", {False}]
        manual = [EncodingData(characters="A", score=12)]
        with self.assertRaises(ValueError):
            encode.frequency_to_encoding_data(mock_file)