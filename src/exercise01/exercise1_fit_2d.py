import logging
import math

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

def fit(x1: float, y1: float, x2: float, y2: float) -> float:
    _logger.debug(f"Points in 2D ({x1}, {y1}) and ({x2}, {y2}).")
    if x2 == x1:
        _logger.error("The two x-coordinates are the same; slope cannot be calculated.")
        return None, None
    else:
        m = (y2 - y1) / (x2 - x1)
        c = y1 - m * x1
        _logger.debug(f"Calculated slope (m): {m}, y-intercept (c): {c}")
        return m, c

def main():
    print ("\n*** Calculate slope and intercept when two points are given in 2D space ***")
    x1 = float(input("Enter x-coordinate of first point: "))
    y1 = float(input("Enter y-coordinate of first point: "))
    x2 = float(input("Enter x-coordinate of second point: "))
    y2 = float(input("Enter y-coordinate of second point: "))

    slope, intercept = fit(x1, y1, x2, y2)
    if slope is None or intercept is None:
        print("Cannot calculate slope and/or intercept.")
    else:
        print(f"The slope 'm' and intercept 'c' for the line passing through points ({x1}, {y1}) and ({x2}, {y2}) are: m={slope}, c={intercept}")

if __name__ == "__main__":
    main()
