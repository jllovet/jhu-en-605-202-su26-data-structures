import unittest
import lab4.sort.merge as merge


class TestSortsProperly(unittest.TestCase):
    def test_empty(self):
        s = merge.sort([])
        self.assertListEqual(s, [])

    def test_single_element_list(self):
            single_element_list = [1]
            s = merge.sort(single_element_list)
            self.assertListEqual(s, single_element_list)
    