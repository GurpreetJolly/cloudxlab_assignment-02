

def compute_iqr(data):
    if not data:
        print("Data list is empty")
        return None
    
    # sort the data
    data = sorted(data)

    q1 = data[round((0.25) * (len(data) - 1))]
    q3 = data[round((0.75) * (len(data) - 1))]
    print(f"Q1 (25th percentile): {q1}")
    print(f"Q3 (75th percentile): {q3}")
    # q1 = np.percentile(data, 25)
    # q3 = np.percentile(data, 75)
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
        print(f"compute_iqr({example_data})")
        print(f"The IQR of the given data is: {compute_iqr(example_data)}")

        example_data = [10, 20, 30, 40, 50, 60]
        print(f"\ncompute_iqr({example_data})")
        print(f"The IQR of the given data is: {compute_iqr(example_data)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
