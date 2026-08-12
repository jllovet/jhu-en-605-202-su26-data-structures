from typing import List
type Algorithm = str
type PivotStrategy = Algorithm

FirstItemPivotToSmallPartitions: Algorithm = "FirstItemPivotToSmallPartitions"
FirstItemPivotInsertionSortForPartitionsLE100: Algorithm = "FirstItemPivotInsertionSortForPartitionsLE100"
FirstItemPivotInsertionSortForPartitionsLE50: Algorithm = "FirstItemPivotInsertionSortForPartitionsLE50"
MedianOfThreePivotToSmallPartitions: Algorithm = "MedianOfThreePivotToSmallPartitions"

FirstItemPivot: PivotStrategy = "FirstItemPivot"
MedianOfThreePivot: PivotStrategy = "MedianOfThreePivot"


class Context:
    def __init__(self, algorithm: Algorithm, xs: List):
        self.algorithm: Algorithm = algorithm
        if algorithm in [
                FirstItemPivotToSmallPartitions,
                FirstItemPivotInsertionSortForPartitionsLE100,
                FirstItemPivotInsertionSortForPartitionsLE50
            ]:
            self.pivot_strategy : PivotStrategy = FirstItemPivot
        elif algorithm == MedianOfThreePivotToSmallPartitions:
            self.pivot_strategy: PivotStrategy = MedianOfThreePivot
        else:
            self.pivot_strategy: PivotStrategy = FirstItemPivot
        self.comparisons: int = 0
        self.list_size: int = len(xs)
        self.xs: List[int] = xs

    def __repr__(self):
        return str(self.__dict__)
