from typing import List, Tuple
import lab4.sort.insertion as insertion

import logging
logger = logging.getLogger(__name__)

type Algorithm = str
FirstItemPivotToSmallPartitions: Algorithm = "FirstItemPivotToSmallPartitions"
FirstItemPivotInsertionSortForPartitionsLE100: Algorithm = "FirstItemPivotInsertionSortForPartitionsLE100"
FirstItemPivotInsertionSortForPartitionsLE50: Algorithm = "FirstItemPivotInsertionSortForPartitionsLE50"
MedianOfThreePivotToSmallPartitions: Algorithm = "MedianOfThreePivotToSmallPartitions"

type PivotStrategy = Algorithm
FirstItemPivot: Algorithm = "FirstItemPivot"
MedianOfThreePivot: Algorithm = "MedianOfThreePivot"


def partition(xs: List[int], strategy: PivotStrategy) -> int:
    if strategy == FirstItemPivot:
        if len(xs) == 0:
            raise ValueError(
                f"Could not determine pivot because the provided list {xs} was empty")
        else:
            return xs[0]
    elif strategy == MedianOfThreePivot:
        if len(xs) < 3:
            raise ValueError(
                f"Could not find median of three for pivot because the list {xs} is too short")
        else:
            low = 0
            high = len(xs) - 1
            mid = (high + low) // 2
            a = xs[low]
            b = xs[mid]
            c = xs[high]
            return median_of_three(a, b, c)
    else:
        raise ValueError(
            "Could not determine pivot because the strategy provided was not valid")


def qs_first_item_pivot_to_small_partitions(xs, ):
    pass


def qs_first_item_pivot_insertion_sort_for_partitions_le_100():
    pass


def qs_first_item_pivot_insertion_sort_for_partitions_le_50():
    pass


def qs_median_of_three_pivot_to_small_partitions():
    pass


def sort(xs, algorithm: Algorithm = FirstItemPivotToSmallPartitions):
    return xs


def median_of_three(a: int, b: int, c: int) -> int:
    items = [a, b, c]
    items.remove(min(items))
    items.remove(max(items))
    return items[0]
