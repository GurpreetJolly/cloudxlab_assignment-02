import logging

logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)

def closer_point(p:tuple, a: tuple, b: tuple) -> float:
    _logger.debug(f"Calculating closest point from {p} and {a} or {p} and {b}.")
    distance_to_b = ((p[0]-b[0])**2 + (p[1]-b[1])**2)**0.5
    distance_to_a = ((p[0]-a[0])**2 + (p[1]-a[1])**2)**0.5
    if distance_to_a < distance_to_b:
        closest = a
    elif distance_to_a > distance_to_b:
        closest = b
    else:
        closest = -1  # Indicate both points are equidistant
    _logger.debug(f"Closest point is: {closest}")
    return closest

def main():
    print ("\n*** Calculate closest point ***")
    p = tuple(map(float, input("Enter point p (x y): ").split()))
    a = tuple(map(float, input("Enter point a (x y): ").split()))
    b = tuple(map(float, input("Enter point b (x y): ").split()))
    closest = closer_point(p, a, b)
    print(f"The closest point to {p} between {a} and {b} is: {'A' if closest == a else 'B' if closest == b else 'Equal'} {closest}")

if __name__ == "__main__":
    main()
