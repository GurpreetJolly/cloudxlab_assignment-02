def multiply_recursive(a: int, b: int) -> int:
    print(f"multiply_recursive called with a={a}, b={b}")
    if b < 0:
        raise ValueError("This function only supports non-negative integers for multiplication.")
    if b == 0:
        return 0
    sum = a + multiply_recursive(a, b - 1)
    print(f"Returning sum={sum} for a={a}, b={b}")
    return sum

def main():
    print("\n*** Multiply two non-negative integers using recursion ***")
    try:
        a = int(input("Enter the first non-negative integer (a): "))
        b = int(input("Enter the second non-negative integer (b): "))
        if a < 0 or b < 0:
            raise ValueError("Both integers must be non-negative.")
        result = multiply_recursive(a, b)
        print(f"The product of {a} and {b} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
