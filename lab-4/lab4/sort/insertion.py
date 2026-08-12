from lab4.sort.context import Context
from typing import List, Tuple

import logging
logger = logging.getLogger(__name__)


def sort(context: Context, xs: List) -> Tuple[Context, List[int]]:
    # Adapted from ZyBook implementation
    logger.debug("in insertion.sort")
    for i in range(1, len(xs)):
        j = i
        # Insert xs[i] into sorted part at correct pos
        while j > 0 and xs[j] < xs[j - 1]:
            # // Swap xs[j] and xs[j - 1]
            logger.debug(
                f"swapping xs[{j}] and xs[{j} - 1]: {xs[j]} and {xs[j - 1]}")
            context.comparisons += 1
            tmp = xs[j]
            xs[j] = xs[j - 1]
            xs[j - 1] = tmp
            j -= 1
    return context, xs
