import argparse
from typing import List, Optional
from .utils import calculate_screw_spacing

def positive_int(value) -> int:
    """
    Validate that the provided value is a positive integer.
    
    :param value: The value to validate.
    :return: The validated integer value.
    :raises argparse.ArgumentTypeError: If the value is not a positive integer.
    """
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
    return ivalue

def parse_arguments(args : Optional[List[str]] = None) -> argparse.Namespace:
    """
    Parse command-line arguments.
    
    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Calculate optimal screw spacings for given stock lengths with whole mm resolution.')
    parser.add_argument('-a', '--atleast', type=positive_int, help='Minimum number of screws (default: 4 times n:r stock)')
    parser.add_argument('-m', '--maximum', type=positive_int, help='Maximum number of screws (default: 10 times n:r stock)')
    parser.add_argument('-e', '--edge-min' , type=positive_int, help='Minimum distance from the end in mm (10)', default=10)
    parser.add_argument('-x', '--edge-max', type=positive_int, help='Maximum distance from the end in mm (50)', default=50)
    parser.add_argument('Lengths', type=positive_int, nargs='+', help='List of stock lengths in mm', metavar='Length')
    return parser.parse_args(args)

def main():
    """
    Main function to calculate and print optimal screw spacings based on provided arguments.
    """
    args = parse_arguments()

    N_min = args.atleast if args.atleast else 4 * len(args.Lengths)
    N_max = args.maximum if args.maximum else 10 * len(args.Lengths)
    
    E_min = args.edge_min
    E_max = args.edge_max

    # validate the input
    if N_min < 2 * len(args.Lengths):
        print(f"Minimum number of screws should be at least {2 * len(args.Lengths)}")
        exit(1)
    
    if N_max < N_min:
        print("Maximum number of screws should be greater than or equal to minimum number of screws")
        exit(1)
    
    if E_max < E_min:
        print("Maximum edge distance should be greater than or equal to minimum edge distance")
        exit(1)
    
    # all stock lengths should be longer than twice the minimum edge distance
    for length in args.Lengths:
        if length < 2 * E_min:
            print(f"All stock lengths should be at least {2 * E_min} mm")
            exit(1)

    # Calculate optimal number of screws
    for n in range(N_min, N_max + 1):
        optimal_result = calculate_screw_spacing(n, E_min, E_max, args.Lengths)
        if optimal_result:
            print(f"{n} screws: {optimal_result.spacing} mm apart")
            
            # Show the results for all lists
            for i, stock in enumerate(optimal_result.stock):
                print(f"  #{i + 1} ({stock.length} mm): {stock.screw_count} holes, edge inset: {stock.inset} mm")
                # show hole positions on the lists
                print("    Drill at: ", end='')
                for j in range(stock.screw_count):
                    if j > 0:
                        print(", ", end='')
                    print(f"{stock.inset + j * optimal_result.spacing} mm", end='')
                print()
        else:
            print(f"{n} screws has no optimal solution.")