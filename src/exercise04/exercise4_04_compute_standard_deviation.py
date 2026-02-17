import math
import exercise04.exercise4_03_compute_mean as compute_mean_module

def compute_sd(numbers) -> float:
    mean = compute_mean_module.compute_mean(numbers)
    squared_total = 0
    for num in numbers:
        squared_total += (num - mean) ** 2
    variance = squared_total / len(numbers)
    sd = math.sqrt(variance)
    return sd

def main():
    print("\n*** Compute Standard Deviation of a List of Numbers ***")
    try:
        input_str = input("Enter numbers separated by spaces: ")
        data = list(map(float, input_str.split()))
        sd_value = compute_sd(data)
        print(f"The standard deviation is: {sd_value}")

        print("\n*** Some more examples ***")
        print(f"compute_sd([2, 4, 4, 4, 5, 5, 7, 9]): {compute_sd([2, 4, 4, 4, 5, 5, 7, 9])}")
        print(f"compute_sd([10, 10, 10]): {compute_sd([10, 10, 10])}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
