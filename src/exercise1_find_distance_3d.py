import logging

logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)

def find_distance_3d(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
    _logger.debug(f"Finding distance between points ({x1}, {y1}, {z1}) and ({x2}, {y2}, {z2}).")
    distance = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2) ** 0.5
    _logger.debug(f"Calculated distance: {distance}")
    return distance

def main():
    print ("\n*** Calculate distance between two points in 3D space ***")
    x1 = float(input("Enter x-coordinate of first point: "))
    y1 = float(input("Enter y-coordinate of first point: "))
    z1 = float(input("Enter z-coordinate of first point: "))
    x2 = float(input("Enter x-coordinate of second point: "))
    y2 = float(input("Enter y-coordinate of second point: "))
    z2 = float(input("Enter z-coordinate of second point: "))

    distance = find_distance_3d(x1, y1, z1, x2, y2, z2)
    print(f"The distance between points ({x1}, {y1}, {z1}) and ({x2}, {y2}, {z2}) is: {distance}")

if __name__ == "__main__":
    main()
