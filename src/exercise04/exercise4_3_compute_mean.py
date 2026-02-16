def compute_mean(numbers) -> float:
    if len(numbers) == 0:
        mean = 0
    else:
        mean = sum(numbers) / len(numbers)
    return mean

def main():
    print("\n*** Compute Mean of a List of Numbers ***")
    try:
        input_str = input("Enter numbers separated by spaces: ")
        data = list(map(float, input_str.split()))
        mean_value = compute_mean(data)
        print(f"The mean is: {mean_value}")

        print("\n*** Some more examples ***")
        print(f"compute_mean([2, 4, 6, 8]): {compute_mean([2, 4, 6, 8])}")
        print(f"compute_mean([10, 20, 30]): {compute_mean([10, 20, 30])}")
        print(f"compute_mean([]): {compute_mean([])}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
