def find_min_max(numbers:list) -> tuple:
    if not numbers:
        raise ValueError("The input list cannot be empty")

    # find minimum value
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num

    # find maximum value
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return (min_value, max_value)

def main():
    print("\n*** Find Minimum and Maximum in a List of Numbers ***")
    input_str = input("Enter numbers separated by spaces: ")
    numbers = list(map(float, input_str.split()))

    try:
        min_value, max_value = find_min_max(numbers)
        print(f"The minimum value is: {min_value}")
        print(f"The maximum value is: {max_value}")

        print("\n*** Some more examples ***")
        print(f"find_min_max([5, 8, 2, 10, 3]): {find_min_max([5, 8, 2, 10, 3])}")
        print(f"find_min_max([7, 7, 7, 7]): {find_min_max([7, 7, 7, 7])}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
