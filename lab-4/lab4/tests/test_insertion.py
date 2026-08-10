import unittest
import lab4.sort.insertion as insertion


class TestSortsProperly(unittest.TestCase):
    def test_empty(self):
        s = insertion.sort([])
        self.assertListEqual(s, [])

    def test_single_element_list(self):
        single_element_list = [1]
        s = insertion.sort(single_element_list)
        self.assertListEqual(s, single_element_list)
