import unittest
import lab4.sort.quick as quick
import random


class TestSortsProperly(unittest.TestCase):
    def test_empty(self):
        s = quick.sort([])
        self.assertListEqual(s, [])

    def test_single_element_list(self):
        single_element_list = [1]
        s = quick.sort(single_element_list)
        self.assertListEqual(s, single_element_list)


class TestPartition(unittest.TestCase):
    def test_partition_on_first_item(self):
        xs = [1, 2, 3]
        self.assertEqual(1, quick.get_pivot(
            xs, strategy=quick.FirstItemPivot))
        xs = []
        with self.assertRaises(ValueError):
            quick.get_pivot(xs, quick.FirstItemPivot)

    def test_partition_on_median_of_three(self):
        xs = [1, 2, 3]
        self.assertEqual(2, quick.get_pivot(
            xs, strategy=quick.MedianOfThreePivot))
        xss = [[1, 2], [1], []]
        for xs in xss:
            with self.assertRaises(ValueError):
                quick.get_pivot(xs, strategy=quick.MedianOfThreePivot)


class TestQuickSortCorrectness(unittest.TestCase):
    def test_qs_first_item_pivot_to_small_partitions(self):
        xs = [random.randrange(0, 1000, 1) for _ in range(50)]
        self.assertListEqual(
            sorted(xs),
            quick.sort(xs, algorithm=quick.FirstItemPivotToSmallPartitions)
        )

    def test_qs_first_item_pivot_insertion_sort_for_partitions_le_100(self):
        xs = [random.randrange(0, 1000, 1) for _ in range(50)]
        self.assertListEqual(
            sorted(xs),
            quick.sort(
                xs, algorithm=quick.FirstItemPivotInsertionSortForPartitionsLE100)
        )

    def test_qs_first_item_pivot_insertion_sort_for_partitions_le_50(self):
        xs = [random.randrange(0, 1000, 1) for _ in range(50)]
        self.assertListEqual(
            sorted(xs),
            quick.sort(
                xs, algorithm=quick.FirstItemPivotInsertionSortForPartitionsLE50)
        )

    def test_qs_median_of_three_pivot_to_small_partitions(self):
        xs = [random.randrange(0, 1000, 1) for _ in range(50)]
        self.assertListEqual(
            sorted(xs),
            quick.sort(xs, algorithm=quick.MedianOfThreePivotToSmallPartitions)
        )


class TestMedianOfThree(unittest.TestCase):
    def test_median_of_three_ascending(self):
        self.assertEqual(quick.median_of_three(1, 2, 3), 2)
        self.assertEqual(quick.median_of_three(1, 2, 2), 2)
        self.assertEqual(quick.median_of_three(2, 2, 2), 2)

    def test_median_of_three_descending(self):
        self.assertEqual(quick.median_of_three(3, 2, 1), 2)
        self.assertEqual(quick.median_of_three(3, 1, 1), 1)
        self.assertEqual(quick.median_of_three(3, 3, 3), 3)

    def test_median_of_three_random(self):
        self.assertEqual(quick.median_of_three(1, 3, 2), 2)
        self.assertEqual(quick.median_of_three(2, 3, 1), 2)
        self.assertEqual(quick.median_of_three(2, 1, 3), 2)
        self.assertEqual(quick.median_of_three(2, 2, 3), 2)
