from typing import List

import logging
logger = logging.getLogger(__name__)


def sort(xs: List) -> List:
    # Adapted from ZyBook implementation
    for i in range(1, len(xs)):
        j = i
        # Insert xs[i] into sorted part at correct pos
        while j > 0 and xs[j] < xs[j - 1]:
            # // Swap xs[j] and xs[j - 1]
            tmp = xs[j]
            xs[j] = xs[j - 1]
            xs[j - 1] = tmp
            j -= 1
    return xs
