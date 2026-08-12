import unittest
import lab4.sort.quick as quick
from lab4.sort.context import Context, FirstItemPivotToSmallPartitions, MedianOfThreePivotToSmallPartitions
import random
import logging
logging.basicConfig(filename="lab4_quick_tests.log",
                    level="DEBUG",
                    format="%(asctime)s - [%(filename)s:%(funcName)s:%(lineno)d] - %(levelname)s - %(message)s",
                    datefmt="%Y-%m-%dT%H:%M:%S%z")

logger = logging.getLogger(__name__)


class TestSortsProperly(unittest.TestCase):
    def test_empty(self):
        _, s = quick.sort(xs=[])
        self.assertListEqual(s, [])

    def test_single_element_list(self):
        single_element_list = [1]
        _, s = quick.sort(xs=single_element_list)
        self.assertListEqual(s, single_element_list)


class TestPartition(unittest.TestCase):
    def test_partition_on_first_item(self):
        xs = [1, 2, 3]
        _, pivot = quick.get_pivot(
            context=Context(algorithm=FirstItemPivotToSmallPartitions, xs=xs),
            xs=xs,
            low_index=0,
            high_index=len(xs)-1)
        self.assertEqual(
            1,
            pivot
        )
        xs = []
        with self.assertRaises(ValueError):
            quick.get_pivot(
                context=Context(algorithm=FirstItemPivotToSmallPartitions, xs=xs),
                xs=xs,
                low_index=0,
                high_index=len(xs)-1)

    def test_partition_on_median_of_three(self):
        xs = [1, 2, 3]
        _, pivot = quick.get_pivot(
            context=Context(algorithm=MedianOfThreePivotToSmallPartitions, xs=xs),
            xs=xs,
            low_index=0,
            high_index=len(xs)-1)
        self.assertEqual(
            2,
            pivot)

        xss = [[1, 2], [1], []]
        for xs in xss:
            with self.assertRaises(ValueError):
                quick.get_pivot(
                    context=Context(algorithm=MedianOfThreePivotToSmallPartitions, xs=xs),
                    xs=xs,
                    low_index=0,
                    high_index=len(xs)-1)


class TestQuickSortCorrectness(unittest.TestCase):
    def test_qs_first_item_pivot_to_small_partitions(self):
        xs = [random.randrange(0, 1000, 1) for _ in range(50)]
        _, res = quick.sort(
            xs, algorithm=quick.FirstItemPivotToSmallPartitions)
        self.assertListEqual(
            sorted(xs),
            res
        )

    def test_qs_first_item_pivot_insertion_sort_for_partitions_le_100(self):
        xs = [random.randrange(0, 1000, 1) for _ in range(50)]
        _, res = quick.sort(
            xs, algorithm=quick.FirstItemPivotInsertionSortForPartitionsLE100)
        self.assertListEqual(
            sorted(xs),
            res
        )

    def test_qs_first_item_pivot_insertion_sort_for_partitions_le_50(self):
        xs = [random.randrange(0, 1000, 1) for _ in range(50)]
        _, res = quick.sort(
            xs, algorithm=quick.FirstItemPivotInsertionSortForPartitionsLE50)
        self.assertListEqual(
            sorted(xs),
            res
        )

    def test_qs_median_of_three_pivot_to_small_partitions(self):
        xs = [random.randrange(0, 1000, 1) for _ in range(50)]
        _, res = quick.sort(
            xs, algorithm=MedianOfThreePivotToSmallPartitions)
        self.assertListEqual(
            sorted(xs),
            res
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
