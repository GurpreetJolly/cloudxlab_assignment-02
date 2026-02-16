from exercise04.exercise4_03_compute_mean import compute_mean
from exercise04.exercise4_04_compute_standard_deviation import compute_sd

def standardization(data):
    if not data:
        print("Data list is empty")
        return None

    mean = compute_mean(data)
    std_dev = compute_sd(data)

    if std_dev == 0 or std_dev is None:
        return [0 for _ in data]
    else:
        return [((x - mean) / std_dev) for x in data]

def main():
    print("\n*** Standardization of a List of Numbers ***")
    try:
        input_str = input("Enter numbers separated by spaces: ")
        data = list(map(float, input_str.split()))
        standardized_data = standardization(data)
        print(f"The standardized data is: {standardized_data}")

        print("\n*** Some more examples ***")

        example_data = [1, 2, 3, 4, 5]
        print(f"standardization({example_data})")
        print(f"The standardized data is: {standardization(example_data)}")

        example_data = [10, 10, 10]
        print(f"\nstandardization({example_data})")
        print(f"The standardized data is: {standardization(example_data)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
