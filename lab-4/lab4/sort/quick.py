from typing import List, Tuple
import lab4.sort.insertion as insertion
from lab4.sort.context import Algorithm, Context, FirstItemPivot, \
    FirstItemPivotToSmallPartitions, FirstItemPivotInsertionSortForPartitionsLE100, \
    FirstItemPivotInsertionSortForPartitionsLE50, MedianOfThreePivotToSmallPartitions, \
    FirstItemPivot, MedianOfThreePivot

import logging
logger = logging.getLogger(__name__)


def get_pivot(context: Context, xs: List[int], low_index: int, high_index: int) -> Tuple[Context, int]:
    if context.pivot_strategy == FirstItemPivot:
        if len(xs) == 0:
            raise ValueError(
                f"Could not determine pivot because the provided list {xs} was empty")
        else:
            logger.debug(f"selecting pivot from index {low_index}: {xs[low_index]}")
            return context, xs[low_index]
    elif context.pivot_strategy == MedianOfThreePivot:
        if len(xs) < 3:
            raise ValueError(
                f"Could not find median of three for pivot because the list {xs} is too short")
        else:
            mid = (high_index + low_index) // 2
            a = xs[low_index]
            b = xs[mid]
            c = xs[high_index]
            context.comparisons += 2
            logger.debug(f"selecting pivot as median of: {a}, {b}, {c}")
            return context, median_of_three(a, b, c)
    else:
        raise ValueError(
            "Could not determine pivot because the strategy provided was not valid")


def partition(context: Context, xs: List[int], low_index: int, high_index: int):
    logger.debug(f"low_index: {low_index}")
    logger.debug(f"high_index: {high_index}")

    context, pivot = get_pivot(context=context, xs=xs, low_index=low_index,
                               high_index=high_index)

    logger.debug(f"pivot: {pivot}")
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

        logger.debug("found items to swap")
        # If zero or one elements remain, then all xs are partitioned
        if low_index >= high_index:
            logger.debug("done with partitioning")
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


def qs_median_of_three_pivot_to_small_partitions(context: Context, xs: List[int], low_index: int, high_index: int) -> Tuple[Context, List[int]]:
    context.algorithm = MedianOfThreePivotToSmallPartitions
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


def sort(xs: List[int], algorithm: Algorithm = FirstItemPivotToSmallPartitions) -> Tuple[Context, List[int]]:
    context = Context(algorithm=algorithm, xs=xs)
    if len(xs) < 2:
        return context, xs
    if algorithm == FirstItemPivotToSmallPartitions:
        logger.info("entering: qs_first_item_pivot_to_small_partitions")
        context, xs = qs_first_item_pivot_to_small_partitions(
            context, xs, low_index=0, high_index=len(xs) - 1)
        logger.info(f"finished quicksort - context: {context}")
        return context, xs

    elif algorithm == FirstItemPivotInsertionSortForPartitionsLE100:
        logger.info(
            "entering: qs_first_item_pivot_insertion_sort_for_partitions_le_100")
        context, xs = qs_first_item_pivot_insertion_sort_for_partitions_le_100(
            context, xs)
        logger.info(f"finished quicksort - context: {context}")
        return context, xs

    elif algorithm == FirstItemPivotInsertionSortForPartitionsLE50:
        logger.info(
            "entering: qs_first_item_pivot_insertion_sort_for_partitions_le_50")
        context, xs = qs_first_item_pivot_insertion_sort_for_partitions_le_50(
            context, xs)
        logger.info(f"finished quicksort - context: {context}")
        return context, xs

    elif algorithm == MedianOfThreePivotToSmallPartitions:
        logger.info("entering: qs_median_of_three_pivot_to_small_partitions")
        context, xs = qs_median_of_three_pivot_to_small_partitions(
            context=context, xs=xs, low_index=0, high_index=len(xs) - 1)
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
