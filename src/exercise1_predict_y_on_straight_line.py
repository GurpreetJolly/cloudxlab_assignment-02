import logging

logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)

def predict(m: float, c: float, x: float) -> float:
    _logger.debug(f"Predicting y for x={x} using line equation y={m}*x + {c}.")
    y = m * x + c
    _logger.debug(f"Predicted y: {y}")
    return y

def main():
    print ("\n*** Predict 'y' on a straight line ***")
    m = float(input("Enter the slope 'm' of the line: "))
    c = float(input("Enter the y-intercept 'c' of the line: "))
    x = float(input("Enter the value of 'x' for which you want to predict 'y': "))

    predicted_y = predict(m, c, x)
    print(f"The predicted value of 'y' for x='{x}' is: {predicted_y}")

if __name__ == "__main__":
    main()
