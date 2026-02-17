from math import exp

def softmax(values, temperature=1.0):
    exp_values =[]

    for value in values:
        exp_value = exp(value/temperature)
        exp_values.append(exp_value)
    sum_exp_values = sum(exp_values)
    ret = []
    for exp_value in exp_values:
        softmax_value = round(exp_value / sum_exp_values, 2)
        ret.append(softmax_value)
    return ret

def main():
    print("\nSoftmax Function with Temperature Example")
    print("-----------------------------------------")
    values = [1, 2, 3]
    temperature = 1.0
    print(f"\nInput values: {values}, temperature: {temperature}")
    softmax_values = softmax(values, temperature)
    print("Softmax values:", softmax_values)

    temperature = 0.5
    print(f"\nInput values: {values}, temperature: {temperature}")
    softmax_values = softmax(values, temperature)
    print("Softmax values:", softmax_values)

    temperature = 2.0
    print(f"\nInput values: {values}, temperature: {temperature}")
    softmax_values = softmax(values, temperature)
    print("Softmax values:", softmax_values)


if __name__ == "__main__":
    main()
