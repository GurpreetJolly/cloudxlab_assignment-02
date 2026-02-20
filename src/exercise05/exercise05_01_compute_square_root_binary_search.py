import sys

def sqrt_binary_search (target:float, tolerance:float, verbose=False) -> tuple[float, bool]:
    """Computes an estimate of the square root of a number."""
    if target < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if target == 1:
        return 1, True
    if target == 0:
        return 0, True
    lower = 0
    if target < 1:
        upper = 1
    else:
        upper = target
    counter = 0
    mid_squared = 0
    max_counter = 10000

    while abs(target-mid_squared) > tolerance and counter < max_counter:
        counter += 1
        if verbose:
            print (f"{counter}. Guessing between {lower} and {upper}")
        mid = (lower + upper) / 2.0
        mid_squared = mid * mid
        if verbose:
            print(f"\tEstimated square root of {target} is approximately {mid}")
        if mid_squared < target:
            lower = mid
        else:
            upper = mid
    return mid, counter < max_counter

###################################
# Start of main program logic
##################################
def main():
    print("\nThis program computes the square root of a number using binary search.")
    verbose = input("Do you want to see the step-by-step process? (y/n): ").strip().lower() == 'y'
    tolerance = 0.00001
    targets = [0, 2, 1]
    for target in targets:
        print(f"\nFinding the square root of {target} with a tolerance of {tolerance}")
        try:
            res, converged = sqrt_binary_search(target, tolerance, verbose)
            if converged:
                print(f"Square root of {target} is approximately {res}")
            else:
                print(f"Failed to converge for target {target}. Best guess is {res}.")    
        except ValueError as e:
            print(f"Error computing square root of {target}: {e}")
            continue

def main_1():
    tolerance = 1e-7    # Accuracy of result is pre-defined here. More precision will require more iterations to converge.

    target = input("\nEnter an integer more than zero to find the square root of: ")
    try:
        if len(target) > 18:
            raise ValueError(f"The input cannot be more than 18 characters long.")
        elif type(target) is not str or not target.isdigit():
            raise ValueError("The input must be a non-negative integer.")
        else:
            target = int(target)
            res = sqrt_binary_search(target, tolerance)
            print(f"Square root of {target} is approximately {res}")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
