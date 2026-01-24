def compute_hcf(x, y):
    """Compute the highest common factor (HCF) of two numbers using the Euclidean algorithm."""
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return compute_hcf(y, x % y)

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    hcf = compute_hcf(num1, num2)
    print(f"The Highest Common Factor of {num1} and {num2} is {hcf}")

if __name__ == "__main__":
    main()    
