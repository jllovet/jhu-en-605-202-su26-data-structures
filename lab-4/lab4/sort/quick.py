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


def get_pivot(context: Context, xs: List[int], low_index: int, high_index: int, strategy: PivotStrategy) -> Tuple[Context, int]:
    if strategy == FirstItemPivot:
        if len(xs) == 0:
            raise ValueError(
                f"Could not determine pivot because the provided list {xs} was empty")
        else:
            return context, xs[low_index]
    elif strategy == MedianOfThreePivot:
        if len(xs) < 3:
            raise ValueError(
                f"Could not find median of three for pivot because the list {xs} is too short")
        else:
            mid = (high_index + low_index) // 2
            a = xs[low_index]
            b = xs[mid]
            c = xs[high_index]
            context.comparisons += 2
            return context, median_of_three(a, b, c)
    else:
        raise ValueError(
            "Could not determine pivot because the strategy provided was not valid")


def partition(context: Context, xs: List[int], low_index: int, high_index: int):
    logger.debug(f"low_index: {low_index}")
    logger.debug(f"high_index: {high_index}")
    context, pivot = get_pivot(context=context, xs=xs, low_index=low_index,
                               high_index=high_index, strategy=FirstItemPivot)
    logger.debug(f"Comparing {xs[low_index]} and {pivot}")
    while True:
        while xs[low_index] < pivot:
            logger.debug(
                f"incrementing low_index: {low_index} -> {low_index + 1}")
            context.comparisons += 1
            low_index += 1
        while pivot < xs[high_index]:
            logger.debug(
                f"decrementing high_index : {high_index} -> {high_index - 1}")
            context.comparisons += 1
            high_index -= 1

        # If zero or one elements remain, then all xs are partitioned
        if low_index >= high_index:
            break
        else:
            logger.debug(f"Swap {xs[low_index]} and {xs[high_index]}")
            temp = xs[low_index]
            xs[low_index] = xs[high_index]
            xs[high_index] = temp

            # // Update low_index and high_index
            low_index += 1
            high_index -= 1
    return context, xs, high_index


def qs_first_item_pivot_to_small_partitions(context: Context, xs: List[int], low_index: int, high_index: int) -> Tuple[Context, List[int]]:
    if not context.algorithm:
        context.algorithm = FirstItemPivotToSmallPartitions
    if high_index <= low_index:
        return context, xs

    context, xs, low_end_index = partition(
        context=context, xs=xs, low_index=low_index, high_index=high_index)

    logger.debug(f"New Low End Index: {low_end_index}")
    # Low partition
    context, xs = qs_first_item_pivot_to_small_partitions(
        context=context, xs=xs, low_index=low_index, high_index=low_end_index)

    # High partition
    context, xs = qs_first_item_pivot_to_small_partitions(
        context=context, xs=xs, low_index=low_end_index+1, high_index=high_index)

    return context, xs


def qs_first_item_pivot_insertion_sort_for_partitions_le_100(context: Context, xs: List[int]) -> Tuple[Context, List[int]]:
    context.algorithm = FirstItemPivotInsertionSortForPartitionsLE100
    # context, pivot = get_pivot(context=context, xs=xs, strategy=FirstItemPivot)
    return context, sorted(xs)


def qs_first_item_pivot_insertion_sort_for_partitions_le_50(context: Context, xs: List[int]) -> Tuple[Context, List[int]]:
    context.algorithm = FirstItemPivotInsertionSortForPartitionsLE50
    # context, pivot = get_pivot(context=context, xs=xs, strategy=FirstItemPivot)
    return context, sorted(xs)


def qs_median_of_three_pivot_to_small_partitions(context: Context, xs: List[int]) -> Tuple[Context, List[int]]:
    context.algorithm = MedianOfThreePivotToSmallPartitions
    # pivot = get_pivot(context=context, xs=xs, strategy=MedianOfThreePivot)
    return context, sorted(xs)


def sort(xs: List[int], algorithm: Algorithm = FirstItemPivotToSmallPartitions) -> Tuple[Context, List[int]]:
    context = Context(algorithm=algorithm, xs=xs)
    if len(xs) < 2:
        return context, xs
    if algorithm == FirstItemPivotToSmallPartitions:
        # print(qs_first_item_pivot_to_small_partitions(context, xs))
        context, xs = qs_first_item_pivot_to_small_partitions(
            context, xs, low_index=0, high_index=len(xs) - 1)
        logger.info(f"finished quicksort - context: {context}")
        return context, xs
    elif algorithm == FirstItemPivotInsertionSortForPartitionsLE100:
        context, xs = qs_first_item_pivot_insertion_sort_for_partitions_le_100(
            context, xs)
        logger.info(f"finished quicksort - context: {context}")
        return context, xs
    elif algorithm == FirstItemPivotInsertionSortForPartitionsLE50:
        context, xs = qs_first_item_pivot_insertion_sort_for_partitions_le_50(
            context, xs)
        logger.info(f"finished quicksort - context: {context}")
        return context, xs
    elif algorithm == MedianOfThreePivotToSmallPartitions:
        context, xs = qs_median_of_three_pivot_to_small_partitions(context, xs)
        logger.info(f"finished quicksort - context: {context}")
        return context, xs
    else:
        raise ValueError(
            "Could not peform quicksort, because an invalid implementation algorithm was provided")


def median_of_three(a: int, b: int, c: int) -> int:
    items = [a, b, c]
    items.remove(min(items))
    items.remove(max(items))
    return items[0]
