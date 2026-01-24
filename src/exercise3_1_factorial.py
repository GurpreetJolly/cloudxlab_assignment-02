def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def main():
    print("\n*** Calculate factorial of a non-negative integer ***")
    try:
        n = int(input("Enter a non-negative integer to compute its factorial: "))
        result = factorial_recursive(n)
        print(f"The factorial of {n} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
