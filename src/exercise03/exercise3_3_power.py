import logging

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

def compute_power(n: int, p: int) -> int:
    _logger.debug(f"power called with n={n}, p={p}")
    if p < 0:
        raise ValueError("This function only supports non-negative integers for exponentiation.")
    if p == 0:
        return 1
    result = n * compute_power(n, p - 1)
    _logger.debug(f"Returning result={result} for n={n}, p={p}")
    return result


def main():
    print("\n*** Calculate n raised to the power of p using recursion ***")
    try:
        n = int(input("Enter the base non-negative integer (n): "))
        p = int(input("Enter the exponent integer (p): "))
        if n < 0:
            raise ValueError("Both integers must be non-negative.")
        result = compute_power(n, abs(p))
        if p < 0:
            result = 1 / result
        print(f"{n} raised to the power of {p} is: {result}")
        print("\nSome other example outputs:")
        print(f"2^3 = {compute_power(2, 3)}")
        print(f"5^2 = {compute_power(5, 2)}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
