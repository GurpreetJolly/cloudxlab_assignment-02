import exercise4_3_compute_mean as compute_mean_module
import exercise4_4_compute_standard_deviation as compute_sd_module

def find_outliers(nums: list, threshold: float) -> list:
    mean = compute_mean_module.compute_mean(nums)
    std_dev = compute_sd_module.compute_sd(nums)
    outliers = []
    for x in nums:
        z = abs(x - mean) / std_dev if std_dev != 0 else 0
        if z > threshold:
            outliers.append(x)
    return outliers

def main():
    print("\n*** Find Outliers in a List of Numbers ***")
    try:
        input_str = input("Enter numbers separated by spaces: ")
        data = list(map(float, input_str.split()))
        threshold = input("Enter the threshold (allowed values 2 or 3): ")
        threshold = float(threshold)
        if threshold not in [2.0, 3.0]:
            raise ValueError("Threshold must be either 2 or 3.")
        outliers = find_outliers(data, threshold)
        if outliers:
            print(f"The outliers are: {outliers}")
        else:
            print("No outliers found.")

        print("\n*** Some more examples ***")
        example_data = [10, 12, 12, 13, 12, 11, 90]
        print(f"find_outliers({example_data}, threshold=2.0): {find_outliers(example_data, 2.0)}")

        example_data = [5, 6, 7, 8, 9, 10, 100]
        print(f"find_outliers({example_data}, threshold=2.0): {find_outliers(example_data, 2.0)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
