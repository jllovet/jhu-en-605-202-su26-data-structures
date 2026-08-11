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

    def test_sorted(self):
        two_asc = [1, 2]
        two_desc = [2, 1]
        three_asc = [1, 2, 3]
        three_desc = [3, 2, 1]
        self.assertEqual([1, 2], insertion.sort(two_asc))
        self.assertEqual([1, 2, 3], insertion.sort(three_asc))
        self.assertEqual(sorted(two_asc), insertion.sort(two_asc))
        self.assertEqual(sorted(two_desc), insertion.sort(two_desc))
        self.assertEqual(sorted(three_asc), insertion.sort(three_asc))
        self.assertEqual(sorted(three_desc), insertion.sort(three_desc))
