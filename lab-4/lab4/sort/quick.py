from typing import List, Tuple
import lab4.sort.insertion as insertion
from lab4.sort.context import Algorithm, Context, FirstItemPivot, \
    FirstItemPivotToSmallPartitions, FirstItemPivotInsertionSortForPartitionsLE100, \
    FirstItemPivotInsertionSortForPartitionsLE50, MedianOfThreePivotToSmallPartitions, \
    FirstItemPivot, MedianOfThreePivot

import logging
logger = logging.getLogger(__name__)


def get_pivot(context: Context, xs: List[int], low_index: int, high_index: int) -> Tuple[Context, int]:
    """Returns the pivot value for Quicksort with context containing runtime metadata about the sorting

    Args:
        context: Context containing runtime metadata about the sorting algorithms
            - Should contain a pivot strategy determined by the algorithm in use. May be one of
                - FirstItemPivot
                - MedianOfThreePivot

        xs: List[int] the list to sort

    Returns:
        Tuple[Context, int] containing the sorting runtime context and the pivot value for Quicksort

    Raises:
        ValueError if the pivot from the provided list was empty

    Side Effects:
        Writes to logs

    Idempotent:
        True
    """
    if context.pivot_strategy == FirstItemPivot:
        if len(xs) == 0:
            raise ValueError(
                f"Could not determine pivot because the provided list {xs} was empty")
        else:
            logger.debug(
                f"selecting pivot from index {low_index}: {xs[low_index]}")
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


def partition(context: Context, xs: List[int], low_index: int, high_index: int) -> Tuple[Context, List[int], int]:
    """Performs the partitioning step of Quicksort and returns the context, the sorted partition,
    and the index of the upper end of the partition within the list

    Args:
        context: Context containing runtime metadata about the sorting algorithms
        xs: List[int] the list to sort
        low_index: int
        high_index: int

    Returns:
        Tuple[Context, List[int], int] containing the sorting runtime context, the sorted partition,
        and index for the upper end of the partition

    Raises:
        None

    Side Effects:
        Writes to logs

    Idempotent:
        True
    """
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
            context.exchanges += 1
            temp = xs[low_index]
            xs[low_index] = xs[high_index]
            xs[high_index] = temp

            # // Update low_index and high_index
            low_index += 1
            high_index -= 1
    return context, xs, high_index


def qs_first_item_pivot_to_small_partitions(context: Context, xs: List[int], low_index: int, high_index: int) -> Tuple[Context, List[int]]:
    """Sorts a list according to the FirstItemPivotToSmallPartitions algorithm

    Args:
        context: Context containing runtime metadata about the sorting algorithms
        xs: List[int] the list to sort
        low_index: int lower end of the partition to be sorted
        high_index: int upper end of the partition to be sorted

    Returns:
        Tuple[Context, List[int]] containing the sorting runtime context and the sorted list

    Raises:
        None

    Side Effects:
        Writes to logs

    Idempotent:
        True
    """
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


def qs_first_item_pivot_insertion_sort_for_partitions_le_100(context: Context, xs: List[int], low_index: int, high_index: int) -> Tuple[Context, List[int]]:
    """Sorts a list according to the FirstItemPivotInsertionSortForPartitionsLE100 algorithm

    Args:
        context: Context containing runtime metadata about the sorting algorithms
        xs: List[int] the list to sort
        low_index: int lower end of the partition to be sorted
        high_index: int upper end of the partition to be sorted

    Returns:
        Tuple[Context, List[int]] containing the sorting runtime context and the sorted list

    Raises:
        None

    Side Effects:
        Writes to logs

    Idempotent:
        True
    """
    if not context.algorithm:
        context.algorithm = FirstItemPivotInsertionSortForPartitionsLE100
    if high_index <= low_index:
        return context, xs

    context, xs, low_end_index = partition(
        context=context, xs=xs, low_index=low_index, high_index=high_index)

    logger.debug(f"New Low End Index: {low_end_index}")

    # Low partition
    if low_end_index - low_index <= 100:
        logger.debug(
            f"switching to insertion sort for low partition, because low_end_index - low_index = {low_end_index - low_index} <= 100")
        to_sort = xs[low_index:low_end_index+1]
        context, sorted_range = insertion.sort(context, to_sort)
        xs[low_index:low_end_index+1] = sorted_range
    else:
        context, xs = qs_first_item_pivot_to_small_partitions(
            context=context, xs=xs, low_index=low_index, high_index=low_end_index)

    # High partition
    if high_index - low_end_index+1 <= 100:
        logger.debug(
            f"switching to insertion sort for high partition, because high_index - low_end_index+1 = {high_index - low_end_index+1} <= 100")
        to_sort = xs[low_end_index+1:high_index+1]
        context, sorted_range = insertion.sort(context, to_sort)
        xs[low_end_index+1:high_index+1] = sorted_range
    else:
        context, xs = qs_first_item_pivot_to_small_partitions(
            context=context, xs=xs, low_index=low_end_index+1, high_index=high_index)

    return context, xs


def qs_first_item_pivot_insertion_sort_for_partitions_le_50(context: Context, xs: List[int], low_index: int, high_index: int) -> Tuple[Context, List[int]]:
    """Sorts a list according to the FirstItemPivotInsertionSortForPartitionsLE50 algorithm

    Args:
        context: Context containing runtime metadata about the sorting algorithms
        xs: List[int] the list to sort
        low_index: int lower end of the partition to be sorted
        high_index: int upper end of the partition to be sorted

    Returns:
        Tuple[Context, List[int]] containing the sorting runtime context and the sorted list

    Raises:
        None

    Side Effects:
        Writes to logs

    Idempotent:
        True
    """
    if not context.algorithm:
        context.algorithm = FirstItemPivotInsertionSortForPartitionsLE50
    if high_index <= low_index:
        return context, xs

    context, xs, low_end_index = partition(
        context=context, xs=xs, low_index=low_index, high_index=high_index)

    logger.debug(f"New Low End Index: {low_end_index}")

    # Low partition
    if low_end_index - low_index <= 50:
        logger.debug(
            f"switching to insertion sort for low partition, because low_end_index - low_index = {low_end_index - low_index} <= 50")
        to_sort = xs[low_index:low_end_index+1]
        context, sorted_range = insertion.sort(context, to_sort)
        xs[low_index:low_end_index+1] = sorted_range
    else:
        context, xs = qs_first_item_pivot_to_small_partitions(
            context=context, xs=xs, low_index=low_index, high_index=low_end_index)

    # High partition
    if high_index - low_end_index+1 <= 50:
        logger.debug(
            f"switching to insertion sort for high partition, because high_index - low_end_index+1 = {high_index - low_end_index+1} <= 50")
        to_sort = xs[low_end_index+1:high_index+1]
        context, sorted_range = insertion.sort(context, to_sort)
        xs[low_end_index+1:high_index+1] = sorted_range
    else:
        context, xs = qs_first_item_pivot_to_small_partitions(
            context=context, xs=xs, low_index=low_end_index+1, high_index=high_index)

    return context, xs


def qs_median_of_three_pivot_to_small_partitions(context: Context, xs: List[int], low_index: int, high_index: int) -> Tuple[Context, List[int]]:
    """Sorts a list according to the MedianOfThreePivotToSmallPartitions algorithm

    Args:
        context: Context containing runtime metadata about the sorting algorithms
        xs: List[int] the list to sort
        low_index: int lower end of the partition to be sorted
        high_index: int upper end of the partition to be sorted

    Returns:
        Tuple[Context, List[int]] containing the sorting runtime context and the sorted list

    Raises:
        None

    Side Effects:
        Writes to logs

    Idempotent:
        True
    """
    context.algorithm = MedianOfThreePivotToSmallPartitions
    if high_index <= low_index:
        return context, xs

    context, xs, low_end_index = partition(
        context=context, xs=xs, low_index=low_index, high_index=high_index)

    logger.debug(f"New Low End Index: {low_end_index}")
    # Low partition
    context, xs = qs_median_of_three_pivot_to_small_partitions(
        context=context, xs=xs, low_index=low_index, high_index=low_end_index)

    # High partition
    context, xs = qs_median_of_three_pivot_to_small_partitions(
        context=context, xs=xs, low_index=low_end_index+1, high_index=high_index)

    return context, xs


def sort(xs: List[int], algorithm: Algorithm = FirstItemPivotToSmallPartitions) -> Tuple[Context, List[int]]:
    """Sorts a list using a user-specified variation of QuickSort

    Args:
        xs: List[int] the list to sort
        algorithm: one of the algorithms that are under examination, defined in context.py
            - FirstItemPivotToSmallPartitions
            - FirstItemPivotInsertionSortForPartitionsLE100
            - FirstItemPivotInsertionSortForPartitionsLE50
            - MedianOfThreePivotToSmallPartitions

    Returns:
        Tuple[Context, List[int]] containing the sorting runtime context and the sorted list

    Raises:
        None

    Side Effects:
        Writes to logs

    Idempotent:
        True
    """
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
            context, xs, low_index=0, high_index=len(xs) - 1)
        logger.info(f"finished quicksort - context: {context}")
        return context, xs

    elif algorithm == FirstItemPivotInsertionSortForPartitionsLE50:
        logger.info(
            "entering: qs_first_item_pivot_insertion_sort_for_partitions_le_50")
        context, xs = qs_first_item_pivot_insertion_sort_for_partitions_le_50(
            context, xs, low_index=0, high_index=len(xs) - 1)
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
    """Returns an int that is the median of a, b, and c"""
    items = [a, b, c]
    items.remove(min(items))
    items.remove(max(items))
    return items[0]
