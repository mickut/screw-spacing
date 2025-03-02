from z3 import Int, Real, Optimize, sat, Abs, Sum
from typing import List, Optional

class StockDefinition:
    length: int
    inset: int
    screw_count: int

    def __init__(self, length: int, inset: int, screw_count: int):
        """
        Initialize a StockDefinition instance.
        :param length: Length of the stock.
        :param inset: Inset distance from the edge.
        :param screw_count: Number of screws.
        """
        self.length = length
        self.inset = inset
        self.screw_count = screw_count

class ScrewCalculationResult:
    screw_count: int
    spacing: int
    stock: List[StockDefinition]

    def __init__(self, screw_count: int, spacing: int, stock: List[StockDefinition]):
        """
        Initialize a ScrewCalculationResult instance.
        :param screw_count: Number of screws.
        :param spacing: Optimal spacing between screws.
        :param stock: List of StockDefinition instances.
        """
        self.screw_count = screw_count
        self.spacing = spacing
        self.stock = stock

def calculate_screw_spacing(screws: int, inset_minimum: int, inset_maximum: int, stock_lengths: List[int]) -> Optional[ScrewCalculationResult]:
    """
    Calculate the optimal screw spacing for given stock lengths.
    :param screws: Total number of screws.
    :param inset_minimum: Minimum edge distance.
    :param inset_maximum: Maximum edge distance.
    :param stock_lengths: List of stock lengths.
    :return: ScrewCalculationResult if a solution is found, otherwise None.
    """
    if screws < 2 * len(stock_lengths):
        return None

    optimizer = Optimize()
    screw_counts, edge_insets, mismatches = [], [], []
    spacing = Int('spacing')
    mismatch = Real('mismatch')

    for i, length in enumerate(stock_lengths):
        screw_count = Int(f'N{i+1}')
        edge_inset = Int(f'E{i+1}')
        length_mismatch = Real(f'mismatch{i+1}')
        
        optimizer.add(screw_count >= 2)
        optimizer.add(edge_inset >= inset_minimum, edge_inset <= inset_maximum, edge_inset <= spacing / 2)
        optimizer.add((screw_count - 1) * spacing + 2 * edge_inset == length)
        optimizer.add(length_mismatch == Abs(length - ((screw_count - 1) * spacing + 2 * edge_inset)))

        screw_counts.append(screw_count)
        edge_insets.append(edge_inset)
        mismatches.append(length_mismatch)

    optimizer.add(Sum(screw_counts) == screws)
    optimizer.add_soft(spacing > 10, 1)
    optimizer.add(mismatch == Sum(mismatches))

    if optimizer.check() == sat:
        model = optimizer.model()
        optimal_spacing = model[spacing].as_long()
        stock = [StockDefinition(length, model[edge_insets[i]].as_long(), model[screw_counts[i]].as_long()) for i, length in enumerate(stock_lengths)]
        return ScrewCalculationResult(screws, optimal_spacing, stock)
    else:
        return None
