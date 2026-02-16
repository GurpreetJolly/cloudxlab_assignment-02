def solve_for_first_variable(equation, vars):
    if len(equation) == len(vars) + 2:
        sum = 0
        for i in range(len(vars)):
            sum += equation[i+1] * vars[i]
        return (equation[len(equation)-1]-sum)/equation[0]
    else:
        ValueError("Parameter length mismatch")
        return None
    
def main():
    print("\n*** Solve for first variable in linear equation with n variables ***")
    equation = [3, 4, 6, 20]
    vars = [5, 6]
    print(f"\nEquation coefficient {equation}")
    print(f"Variable values from 2nd onwards {vars}")
    ret = solve_for_first_variable(equation, vars)
    if ret == None:
        print("Error finding value")
    else:
        print(f"Solution of 'x' = {ret}")

    equation = [2, 5, 7]
    vars = [4]
    print(f"\nEquation coefficient {equation}")
    print(f"Variable values from 2nd onwards {vars}")
    ret = solve_for_first_variable(equation, vars)
    if ret == None:
        print("Error finding value")
    else:
        print(f"Solution of 'x' = {ret}")

if __name__ == "__main__":
    main()
