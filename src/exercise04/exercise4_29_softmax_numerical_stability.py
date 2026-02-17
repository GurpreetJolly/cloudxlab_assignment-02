from math import exp

def softmax(values):
    exp_values =[]
    max_value = max(values)

    for value in values:
        exp_value = exp(value-max_value)
        exp_values.append(exp_value)
    sum_exp_values = sum(exp_values)
    ret = []
    for exp_value in exp_values:
        softmax_value = round(exp_value / sum_exp_values, 2)
        ret.append(softmax_value)
    return ret

def main():
    print("\nSoftmax Function with Numerical Stability Example")
    values = [1, 2, 3]
    softmax_values = softmax(values)
    print("\nInput values:", values)
    print("Softmax values:", softmax_values)

    values = [1000, 1001, 1002]
    softmax_values = softmax(values)
    print("\nInput values:", values)
    print("Softmax values:", softmax_values)

if __name__ == "__main__":
    main()
