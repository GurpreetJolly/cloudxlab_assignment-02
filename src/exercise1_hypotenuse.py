import logging

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

def calculate_hypotenuse(a: float, b: float) -> float:
    _logger.debug(f"Calculating hypotenuse for sides a={a}, b={b}.")
    hypotenuse = (a**2 + b**2) ** 0.5
    _logger.debug(f"Calculated hypotenuse: {hypotenuse}")
    return hypotenuse

def main():
    print ("\n*** Calculate hypotenuse of a right angle triangle ***")
    a = float(input("Enter length of side Base: "))
    b = float(input("Enter length of side Height: "))

    hypotenuse = calculate_hypotenuse(a, b)
    print(f"The hypotenuse of a right angle triangle with Base {a} and Height {b} is: {hypotenuse}")

if __name__ == "__main__":
    main()
