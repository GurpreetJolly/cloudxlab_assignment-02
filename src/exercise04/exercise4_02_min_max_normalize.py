import exercise04.exercise4_01_min_max as exercise4_01_min_max 

def min_max_normalize(value, data) -> float:
    if not data:
        raise ValueError("The data list cannot be empty")

    # Use previously defined function to find min and max
    min_value, max_value = exercise4_01_min_max.find_min_max(data)

    if max_value == min_value:
        raise ValueError("All values in the data list are the same; normalization is not possible.")

    normalized_value = (value - min_value) / (max_value - min_value)
    return normalized_value

def main():
    print("\n*** Min-Max Normalization ***")
    try:
        input_str = input("Enter numbers separated by spaces: ")
        data = list(map(float, input_str.split()))

        value = float(input("Enter the value to normalize: "))
        normalized = min_max_normalize(value, data)
        print(f"The normalized value of {value} is: {normalized}")

        print("\n*** Some more examples ***")
        example_data = [10, 20, 30]
        example_value = 20
        print(f"min_max_normalize({example_value}, {example_data}): {min_max_normalize(example_value, example_data)}")

        example_value = 10
        print(f"min_max_normalize({example_value}, {example_data}): {min_max_normalize(example_value, example_data)}")

    except ValueError as e:
        print(e)
    
if __name__ == "__main__":
    main()
