def normalize_to_probabilities(numbers):
    total = sum(numbers)
    if total == 0:
        raise ValueError("The sum of the numbers must be greater than zero.")
    ret = []
    for num in numbers:
        ret.append(round(num / total, 2))
    return ret

def main():
    print("Normalize a List into Probabilities")
    numbers = [1, 2, 3]
    probabilities = normalize_to_probabilities(numbers)
    print(f"\nNumbers: {numbers}")
    print(f"Normalized Probabilities: {probabilities}")

    numbers = [3, 3, 4]
    probabilities = normalize_to_probabilities(numbers)
    print(f"\nNumbers: {numbers}")
    print(f"Normalized Probabilities: {probabilities}")

if __name__ == "__main__":
    main()
