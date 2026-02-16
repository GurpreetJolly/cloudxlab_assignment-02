def compute_rmse(actual, predicted):
    if len(actual) != len(predicted):
        raise ValueError("The length of actual and predicted lists must be the same.")

    n = len(actual)
    squared_errors = [(a - p) ** 2 for a, p in zip(actual, predicted)]
    mean_squared_error = sum(squared_errors) / n
    rmse = mean_squared_error ** 0.5

    return rmse

def main():
    print("*** Exercise 4.8: Root Mean Squared Error (RMSE) Calculation ***")
    print("*** \nSome sample examples to test your compute_rmse function ***")
    # Example usage
    actual = [2, 3, 4]
    predicted = [3, 2, 5]
    rmse_value = compute_rmse(actual, predicted)
    print(f"\ncompute_rmse({actual}, {predicted})\tRMSE: {rmse_value}")

    actual = [1, 2, 3]
    predicted = [1, 2, 3]
    rmse_value = compute_rmse(actual, predicted)
    print(f"\ncompute_rmse({actual}, {predicted})\tRMSE: {rmse_value}")

    actual = [2, 3, 4]
    predicted = [3, 1, 7]
    rmse_value = compute_rmse(actual, predicted)
    print(f"\ncompute_rmse({actual}, {predicted})\tRMSE: {rmse_value}")

if __name__ == "__main__":
    main()

