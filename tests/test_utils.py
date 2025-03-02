import pytest
from screw_spacing.utils import calculate_screw_spacing, StockDefinition, ScrewCalculationResult

def test_calculate_screw_spacing_valid():
    screw_count = 10
    inset_minimum = 5
    inset_maximum = 15
    StockLengths = [400, 600, 400]

    result = calculate_screw_spacing(screw_count, inset_minimum, inset_maximum, StockLengths)

    assert result is not None
    assert result.screw_count == screw_count
    assert result.spacing > 0
    assert len(result.stock) == len(StockLengths)
    for stock in result.stock:
        assert stock.length in StockLengths
        assert inset_minimum <= stock.inset <= inset_maximum
        assert stock.screw_count >= 2


def test_calculate_screw_spacing_insufficient_screws():
    screw_count = 5
    inset_minimum = 5
    inset_maximum = 15
    StockLengths = [100, 150, 200]

    result = calculate_screw_spacing(screw_count, inset_minimum, inset_maximum, StockLengths)

    assert result is None

def test_calculate_screw_spacing_no_solution():
    screw_count = 10
    inset_minimum = 50
    inset_maximum = 60
    StockLengths = [100, 150, 200]

    result = calculate_screw_spacing(screw_count, inset_minimum, inset_maximum, StockLengths)

    assert result is None