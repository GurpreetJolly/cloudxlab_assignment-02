from exercise04.exercise4_03_compute_mean import compute_mean

def compute_mae_2d(actual, predicted) -> float:
    absolute_errors = []
    for actual_row, predicted_row in zip(actual, predicted):
        for a, p in zip(actual_row, predicted_row):
            absolute_errors.append(abs(a - p))
    if not absolute_errors:
        return 0.0
    return compute_mean(absolute_errors)


def compute_mae(actual, predicted) -> float:
    absolute_errors = [abs(a - p) for a, p in zip(actual, predicted)]
    if not absolute_errors:
        return 0.0
    return compute_mean(absolute_errors)

def main():
    print("Exercise 4.9: Mean Absolute Error (MAE) Calculation")
    print("\n*** Example - 1D Data ***")
    actual = [3, 5, 2]
    predicted = [2, 5, 4]
    print(f"Actual 1D data: {actual}")
    print(f"Predicted 1D data: {predicted}")
    mae = compute_mae(actual, predicted)
    print(f"Mean Absolute Error for 1D data: {mae}")

    print("\n*** Example - 2D Data ***")
    actual_2d = [[1, 2], [3, 4], [5, 6]]
    predicted_2d = [[2, 2], [2, 5], [5, 7]]
    print(f"Actual 2D data: {actual_2d}")
    print(f"Predicted 2D data: {predicted_2d}")
    mae_2d = compute_mae_2d(actual_2d, predicted_2d)
    print(f"Mean Absolute Error for 2D data: {mae_2d}")

if __name__ == "__main__":
    main()