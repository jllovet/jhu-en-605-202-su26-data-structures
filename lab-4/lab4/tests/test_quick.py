import unittest
import lab4.sort.quick as quick


class TestSortsProperly(unittest.TestCase):
    def test_empty(self):
        s = quick.sort([])
        self.assertListEqual(s, [])

    def test_single_element_list(self):
            single_element_list = [1]
            s = quick.sort(single_element_list)
            self.assertListEqual(s, single_element_list)
    