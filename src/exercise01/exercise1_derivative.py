import logging
import math

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

def square(x):
    return x**2
def cube(x):
    return x**3
def sine(x):
    return math.sin(x)
def cosine(x):
    return math.cos(x)

def approx_derivative(f, x: float, h: float = 1e-5) -> float:
    _logger.debug(f"Approximating derivative of function at x={x} with h={h}.")
    derivative = (f(x + h) - f(x)) / h
    _logger.debug(f"Calculated approximate derivative: {derivative}")
    return derivative

def main():
    print ("\n*** Calculate approximate derivative of a function ***")
    print ("\t***************************************")
    print ("\t**************** Menu *****************")
    print ("\t***************************************")
    print ("\t* 1. f(x) = Square function (x^2)     *")
    print ("\t* 2. f(x) = Cube function (x^3)       *")
    print ("\t* 3. f(x) = Sine function (sin(x))    *")
    print ("\t* 4. f(x) = Cosine function (cos(x))  *")
    print ("\t***************************************")
    choice = input("Enter the number for which you want to find approximate derivative: ")

    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice. Choose either 1 to 4. Computation aborted.")
    else:
        if choice in {"1", "2"}:
            x = float(input("Enter the point 'x' at which to approximate the derivative: "))
        elif choice in {"3", "4"}:
            x = float(input("Enter the angle 'x' (in degrees) at which to approximate the derivative: "))
        else:
            print("Invalid choice. Choose either 1 to 4. Computation aborted.")
            return

        if choice == "1":
            f = square
        elif choice == "2":
            f = cube
        elif choice == "3":
            x = math.radians(x)
            f = sine
        elif choice == "4":
            x = math.radians(x)
            f = cosine
        else:
            print("Invalid choice. Choose either 1 to 4. Computation aborted.")
            return

        derivative = approx_derivative(f, x)
        if choice in {"1", "2"}:
            print(f"The approximate derivative of f(x) = {f.__name__} at x={x} is: {derivative}")
        elif choice in {"3", "4"}:
            print(f"The approximate derivative of f(x) = {f.__name__} at x={math.degrees(x)} degrees is: {derivative}")

if __name__ == "__main__":
    main()
