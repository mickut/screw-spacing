import pytest
import argparse
from screw_spacing.main import positive_int, parse_arguments

def test_positive_int():
    assert positive_int("5") == 5
    assert positive_int("1") == 1
    with pytest.raises(argparse.ArgumentTypeError):
        positive_int("0")
    with pytest.raises(argparse.ArgumentTypeError):
        positive_int("-1")
    with pytest.raises(ValueError):
        positive_int("abc")

def test_parse_arguments_with_all_options():
    args = parse_arguments(['-a', '5', '-m', '10', '-e', '15', '-x', '20', '100', '200'])
    assert args.atleast == 5
    assert args.maximum == 10
    assert args.edge_min == 15
    assert args.edge_max == 20
    assert args.Lengths == [100, 200]

def test_parse_arguments_with_default_options():
    args = parse_arguments(['100', '200'])
    assert args.atleast is None
    assert args.maximum is None
    assert args.edge_min == 10
    assert args.edge_max == 50
    assert args.Lengths == [100, 200]

def test_parse_arguments_no_arguments():
    with pytest.raises(SystemExit):
        parse_arguments([])

def test_parse_arguments_invalid_atleast():
    with pytest.raises(SystemExit):
        parse_arguments(['-a', '-1', '100'])

def test_parse_arguments_invalid_maximum():
    with pytest.raises(SystemExit):
        parse_arguments(['-m', '0', '100'])

if __name__ == "__main__":
    pytest.main()