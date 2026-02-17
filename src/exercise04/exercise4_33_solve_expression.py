# This is first attempt. The function works fine but next one is optimized.
def solve_expression(expr):
    flat_list = []
    all_single_values = True
    for item in expr:
        if isinstance(item, list):
            all_single_values = False
            res = solve_expression(item)
            flat_list.extend(res)  # Recursively flatten the sublist
        else:
            all_single_values = True
            flat_list.append(item)  # Append non-list items directly
    if all_single_values:
        if flat_list[0] == "+":
            return [flat_list[1] + flat_list[2]]
        elif flat_list[0] == "*":
            return [flat_list[1] * flat_list[2]]
        elif flat_list[0] == "-":
            return [flat_list[1] - flat_list[2]]
        elif flat_list[0] == "/":
            return [flat_list[1] / flat_list[2]]

    return flat_list

# Final version
def solve_expression_1(expr):
    if isinstance(expr, list):
        operator = expr[0]
        operand1 = solve_expression_1(expr[1])
        operand2 = solve_expression_1(expr[2])
        
        if operator == "+":
            return operand1 + operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "/":
            return operand1 / operand2
    else:
        return expr

def main():
    print("\nSolve Expression Examples")
    print("---------------------------")

    in_list = ["*", ["+", 20, 40], 90]
    print(f"\nExample 1: Solve expression {in_list}")
    result = solve_expression_1(in_list)
    print("Result:", result)

    in_list = ["-", ["*", ["/", 100, 10], 5], 15]
    print(f"\nExample 2: Solve expression {in_list}")
    result = solve_expression_1(in_list)
    print("Result:", result)

if __name__ == "__main__":
    main()
