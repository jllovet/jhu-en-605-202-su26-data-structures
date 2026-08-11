from typing import List, Tuple
import lab4.sort.insertion as insertion
from lab4.sort.context import Algorithm, Context

import logging
logger = logging.getLogger(__name__)

FirstItemPivotToSmallPartitions: Algorithm = "FirstItemPivotToSmallPartitions"
FirstItemPivotInsertionSortForPartitionsLE100: Algorithm = "FirstItemPivotInsertionSortForPartitionsLE100"
FirstItemPivotInsertionSortForPartitionsLE50: Algorithm = "FirstItemPivotInsertionSortForPartitionsLE50"
MedianOfThreePivotToSmallPartitions: Algorithm = "MedianOfThreePivotToSmallPartitions"

type PivotStrategy = Algorithm
FirstItemPivot: Algorithm = "FirstItemPivot"
MedianOfThreePivot: Algorithm = "MedianOfThreePivot"


def get_pivot(context: Context, xs: List[int], strategy: PivotStrategy) -> Tuple[Context, int]:
    if strategy == FirstItemPivot:
        if len(xs) == 0:
            raise ValueError(
                f"Could not determine pivot because the provided list {xs} was empty")
        else:
            return context, xs[0]
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
            context.comparisons += 2
            return context, median_of_three(a, b, c)
    else:
        raise ValueError(
            "Could not determine pivot because the strategy provided was not valid")


def qs_first_item_pivot_to_small_partitions(context: Context, xs: List[int]) -> Tuple[Context, List[int]]:
    context.algorithm = FirstItemPivotToSmallPartitions
    context, pivot = get_pivot(context=context, xs=xs, strategy=FirstItemPivot)
    return context, sorted(xs)


def qs_first_item_pivot_insertion_sort_for_partitions_le_100(context: Context, xs: List[int]) -> Tuple[Context, List[int]]:
    context.algorithm = FirstItemPivotInsertionSortForPartitionsLE100
    context, pivot = get_pivot(context=context, xs=xs, strategy=FirstItemPivot)
    return context, sorted(xs)


def qs_first_item_pivot_insertion_sort_for_partitions_le_50(context: Context, xs: List[int]) -> Tuple[Context, List[int]]:
    context.algorithm = FirstItemPivotInsertionSortForPartitionsLE50
    context, pivot = get_pivot(context=context, xs=xs, strategy=FirstItemPivot)
    return context, sorted(xs)


def qs_median_of_three_pivot_to_small_partitions(context: Context, xs: List[int]) -> Tuple[Context, List[int]]:
    context.algorithm = MedianOfThreePivotToSmallPartitions
    pivot = get_pivot(context=context, xs=xs, strategy=MedianOfThreePivot)
    return context, sorted(xs)


def sort(xs: List[int], algorithm: Algorithm = FirstItemPivotToSmallPartitions) -> Tuple[Context, List[int]]:
    context = Context(algorithm=algorithm)
    if len(xs) < 2:
        return context, xs
    if algorithm == FirstItemPivotToSmallPartitions:
        return qs_first_item_pivot_to_small_partitions(context, xs)
    elif algorithm == FirstItemPivotInsertionSortForPartitionsLE100:
        return qs_first_item_pivot_insertion_sort_for_partitions_le_100(context, xs)
    elif algorithm == FirstItemPivotInsertionSortForPartitionsLE50:
        return qs_first_item_pivot_insertion_sort_for_partitions_le_50(context, xs)
    elif algorithm == MedianOfThreePivotToSmallPartitions:
        return qs_median_of_three_pivot_to_small_partitions(context, xs)
    else:
        raise ValueError(
            "Could not peform quicksort, because an invalid implementation algorithm was provided")


def median_of_three(a: int, b: int, c: int) -> int:
    items = [a, b, c]
    items.remove(min(items))
    items.remove(max(items))
    return items[0]
