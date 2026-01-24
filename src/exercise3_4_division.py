import logging

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

def recursive_divide(n: int, d: int) -> tuple:
    _logger.debug(f"recursive_divide called with n={n}, d={d}")
    if d == 0:
        raise ValueError("Division by zero is not allowed.")
    if n < d:
        return (0, n)
    result = (1 + recursive_divide(n - d, d)[0], recursive_divide(n - d, d)[1])
    _logger.debug(f"Returning result={result} for n={n}, d={d}")
    return result

def main():
    print("\n*** Calculate integer division n // d using recursion ***")
    try:
        n = int(input("Enter the dividend non-negative integer (n): "))
        d = int(input("Enter the divisor positive integer (d): "))
        if n < 0 or d <= 0:
            raise ValueError("Dividend must be non-negative and divisor must be positive.")
        result = recursive_divide(n, d)
        print(f"The result of {n} // {d} is: {result}")

        print("\nSome other example outputs:")
        print(f"17 // 5 = {recursive_divide(17, 5)}")
        print(f"20 // 4 = {recursive_divide(20, 4)}")
        print(f" 7 // 3 = {recursive_divide(7, 3)}")
        print(f" 0 // 1 = {recursive_divide(0, 1)}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
