# screw-spacing

Calculates even hole spacing to lengths of stock, e.g. for attaching rails with screws.

## Features

- Calculate even spacing for screws along lengths of stock.
- Command-line interface for easy usage.
- Utilizes Z3 solver for precise calculations.

## Installation

You can install the package using `pip`:

```sh
pip install git+https://github.com/mickut/screw-spacing.git
```

## Usage
After installation, you can use the command-line tool as follows:

```sh
screw-spacing 400 600
```

### Command-line Options

```
  -a ATLEAST, --atleast ATLEAST
                        Minimum number of screws (default: 4 n:r stock)
  -m MAXIMUM, --maximum MAXIMUM
                        Maximum number of screws (default: 10 times n:r stock)
  -e EDGE_MIN, --edge-min EDGE_MIN
                        Minimum distance from the end in mm (10)
  -x EDGE_MAX, --edge-max EDGE_MAX
                        Maximum distance from the end in mm (50)
```

### Example

```sh
screw-spacing -a 10 -m 15 -e 15 -x 30 600 500 400
```

This will output the positions of the screws along the length of the stock for any solutions:

```
10 screws has no optimal solution.
11 screws has no optimal solution.
12 screws has no optimal solution.
13 screws has no optimal solution.
14 screws has no optimal solution.
15 screws: 114 mm apart
  #1 (600 mm): 6 holes, edge inset: 15 mm
    Drill at: 15 mm, 129 mm, 243 mm, 357 mm, 471 mm, 585 mm
  #2 (500 mm): 5 holes, edge inset: 22 mm
    Drill at: 22 mm, 136 mm, 250 mm, 364 mm, 478 mm
  #3 (400 mm): 4 holes, edge inset: 29 mm
    Drill at: 29 mm, 143 mm, 257 mm, 371 mm
```

## Development
To contribute to the development of this tool, follow these steps:

Clone the repository:

```sh
git clone https://github.com/yourusername/screw-spacing.git
```

Navigate to the project directory:

```sh
cd screw-spacing
```

Install the dependencies:

```sh
pip install -r requirements.txt
```

Run the tests:

```sh
pytest
```


## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or suggestions, please open an issue on the GitHub repository.