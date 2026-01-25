import numpy as np

def compute_iqr(data):
    if not data:
        raise ValueError("Data list is empty")

    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    print(f"Q1 (25th percentile): {q1}")
    print(f"Q3 (75th percentile): {q3}")
    iqr = q3 - q1
    return iqr

def main():
    print("\n*** Compute Interquartile Range (IQR) of a List of Numbers ***")
    try:
        input_str = input("Enter numbers separated by spaces: ")
        data = list(map(float, input_str.split()))
        iqr = compute_iqr(data)
        print(f"The IQR of the given data is: {iqr}")

        print("\n*** Some more examples ***")
        example_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(f"compute_iqr({example_data}): {compute_iqr(example_data)}")

        example_data = [10, 20, 30, 40, 50, 60]
        print(f"compute_iqr({example_data}): {compute_iqr(example_data)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
