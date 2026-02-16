def huber_loss(y_true, y_pred, delta=1.0):
    if len(y_true) != len(y_pred):
        raise ValueError("The length of y_true and y_pred must be the same.")

    loss = 0.0
    for true, pred in zip(y_true, y_pred):
        error = true - pred
        if abs(error) <= delta:
            loss += 0.5 * error ** 2
            print(f"For ({true}, {pred}): Squared Loss = 0.5 * {error:.4f} ** 2 = {round(0.5 * error ** 2, 4)}")
        else:
            loss += delta * abs(error) - 0.5 * delta ** 2
            print(f"For ({true}, {pred}): Linear Loss = {delta} * |{error:.4f}| - 0.5 * {delta} ** 2 = {round(delta * abs(error) - 0.5 * delta ** 2, 4)}")

    return loss / len(y_true)

def main():
    print("*** Huber Loss Calculation Example ***")
    # Example usage
    y_true = [5, 2, 7]
    y_pred = [4.8, 2.5, 10]
    delta = 1.0
    print(f"\nTrue values {y_true}, predicted values {y_pred}, delta = {delta}")
    loss = huber_loss(y_true, y_pred, delta)
    print(f"Huber Loss: {loss:.4f}")

    y_true = [1, 2, 3]
    y_pred = [1, 2, 3]
    delta = 1.0
    print(f"\nTrue values {y_true}, predicted values {y_pred}, delta = {delta}")
    loss = huber_loss(y_true, y_pred, delta)
    print(f"Huber Loss: {loss:.4f}")

if __name__ == "__main__":
    main()
