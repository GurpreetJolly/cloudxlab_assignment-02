from math import exp
import random

def weighted_choice_with_temperature(weights, temperature=1.0):
    if temperature <= 0:
        raise ValueError("Temperature must be greater than 0.")

    weighted_values =[]

    for value in weights:
        weighted_value = exp(value**(1/temperature))
        weighted_values.append(weighted_value)
    sum_weighted_values = sum(weighted_values)
    ret = []
    for weighted_value in weighted_values:
        normalized_value = round(weighted_value / sum_weighted_values, 4)
        ret.append(normalized_value)

    return ret[random.randint(0, len(weights) - 1)] # Need to fix this.

def main():
    user_msg = "Need to understand better the return value of the function. Not clear from the exercise description."
    print(f"{NotImplementedError(user_msg)}")
    return
    #raise NotImplementedError(user_msg)

    print("\nWeighted choices with Temperature Example")
    print("-----------------------------------------")
    values = [1, 2, 3]
    temperature = 1.0
    print(f"\nInput values: {values}, temperature: {temperature}")
    softmax_values = weighted_choice_with_temperature(values, temperature)
    print("Softmax values:", softmax_values)

    temperature = 0.5
    print(f"\nInput values: {values}, temperature: {temperature}")
    softmax_values = weighted_choice_with_temperature(values, temperature)
    print("Softmax values:", softmax_values)

    temperature = 2.0
    print(f"\nInput values: {values}, temperature: {temperature}")
    softmax_values = weighted_choice_with_temperature(values, temperature)
    print("Softmax values:", softmax_values)


if __name__ == "__main__":
    main()
