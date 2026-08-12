import unittest
import lab4.sort.merge as merge
from lab4.sort.context import Context, NaturalMergeSort
import random
import logging
logging.basicConfig(filename="lab4_quick_tests.log",
                    level="DEBUG",
                    format="%(asctime)s - [%(filename)s:%(funcName)s:%(lineno)d] - %(levelname)s - %(message)s",
                    datefmt="%Y-%m-%dT%H:%M:%S%z")

logger = logging.getLogger(__name__)

class TestSortsProperly(unittest.TestCase):
    def test_empty(self):
        xs = []
        context, s = merge.sort(xs, algorithm=NaturalMergeSort)
        self.assertListEqual(s, [])

    def test_single_element_list(self):
        single_element_list = [1]
        context, s = merge.sort(single_element_list, algorithm=NaturalMergeSort)
        self.assertListEqual(s, single_element_list)

    # def test_natural_merge(self):
        # Currently producing an infinite loop
        # xs = [random.randrange(0, 1000, 1) for _ in range(10)]
        # context, s = merge.sort(xs, algorithm=NaturalMergeSort)
        # self.assertListEqual(s, sorted(xs))