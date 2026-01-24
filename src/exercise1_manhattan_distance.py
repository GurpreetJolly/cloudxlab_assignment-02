import logging

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

def manhattan_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    _logger.debug(f"Finding Manhattan distance between points ({x1}, {y1}) and ({x2}, {y2}).")
    distance = abs(x2 - x1) + abs(y2 - y1)
    _logger.debug(f"Calculated Manhattan distance: {distance}")
    return distance

def main():
    print ("\n*** Calculate Manhattan distance between two points in 2D space ***")
    x1 = float(input("Enter x-coordinate of first point: "))
    y1 = float(input("Enter y-coordinate of first point: "))
    x2 = float(input("Enter x-coordinate of second point: "))
    y2 = float(input("Enter y-coordinate of second point: "))

    distance = manhattan_distance(x1, y1, x2, y2)
    print(f"The Manhattan distance between points ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")

if __name__ == "__main__":
    main()

