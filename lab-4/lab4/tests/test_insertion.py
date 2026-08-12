import unittest
import lab4.sort.insertion as insertion
from lab4.sort.context import Context, FirstItemPivotInsertionSortForPartitionsLE100


class TestSortsProperly(unittest.TestCase):
    def test_empty(self):
        xs = []
        context = Context(FirstItemPivotInsertionSortForPartitionsLE100, xs=xs)
        context, s = insertion.sort(context, xs)
        self.assertListEqual(s, [])

    def test_single_element_list(self):
        single_element_list = [1]
        context = Context(
            FirstItemPivotInsertionSortForPartitionsLE100, xs=single_element_list)
        context, s = insertion.sort(context, single_element_list)
        self.assertListEqual(s, single_element_list)

    def test_sorted(self):
        two_asc = [1, 2]
        two_desc = [2, 1]
        three_asc = [1, 2, 3]
        three_desc = [3, 2, 1]
        dummy_context = Context(
            FirstItemPivotInsertionSortForPartitionsLE100, xs=[])

        self.assertEqual([1, 2],
                         insertion.sort(dummy_context, two_asc)[1])

        self.assertEqual([1, 2, 3],
                         insertion.sort(dummy_context, three_asc)[1])

        self.assertEqual(sorted(two_asc),
                         insertion.sort(dummy_context, two_asc)[1])

        self.assertEqual(sorted(two_desc),
                         insertion.sort(dummy_context, two_desc)[1])

        self.assertEqual(sorted(three_asc),
                         insertion.sort(dummy_context, three_asc)[1])

        self.assertEqual(sorted(three_desc),
                         insertion.sort(dummy_context, three_desc)[1])
