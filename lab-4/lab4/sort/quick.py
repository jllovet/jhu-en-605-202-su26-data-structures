from typing import List, Tuple
import lab4.sort.insertion as insertion

import logging
logger = logging.getLogger(__name__)


def sort(xs):
    return xs


def median_of_three(a: int, b: int, c: int) -> int:
    items = [a, b, c]
    items.remove(min(items))
    items.remove(max(items))
    return items[0]
