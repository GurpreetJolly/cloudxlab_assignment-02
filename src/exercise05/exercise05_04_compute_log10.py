import sys

def log10_binary_search(x, tolerance, verbose=False) -> tuple[float, bool]:
    if x <= 0:
        raise ValueError("Input must be a positive integer.")
    
    counter = 0
    mid_log10 = 0
    max_iterations = 10000

    lower = 0 if x >= 1 else -100  # Log10 of numbers less than 1 is negative, so we set lower to -100 for those cases.
    upper = max(1, len(str(x)))  # Log10 of numbers less than 1 is negative, so we set upper to 1 for those cases.
    
    while abs(x - mid_log10) > tolerance and counter < max_iterations:
        counter += 1
        if verbose:
            print(f"{counter}. Guessing between {lower} and {upper}")
        mid = (lower + upper) / 2.0
        mid_log10 = 10**mid
        if verbose:
            print(f"\tEstimated log10 of {x} is approximately {mid}")
        if mid_log10 < x:
            lower = mid
        else:
            upper = mid

    if counter >= max_iterations:
        raise ValueError(f"Failed to converge after {counter} iterations. Last guess was {mid} with power {mid_log10}")
    return mid, True


###################################
# Start of main program logic
##################################
def main():
    print("\n*** Computes the log10 of a number using binary search. ***")
    tolerance = 1e-7    # Accuracy of result is pre-defined here. More precision will require more iterations to converge.
    verbose = input("Do you want to see the step-by-step process? (y/n): ").strip().lower() == 'y'
    tolerance = 1e-4
    targets = [100, 1000, 0.01, 2]

    for target in targets:    
        print(f"\nFinding log10 of {target} with a tolerance of {tolerance}")
        try:
            result,converged = log10_binary_search(target, tolerance, verbose)
            if converged:
                print(f"Result: {result}")
            else:
                print(f"Failed to converge for target {target}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    return 0

if __name__ == "__main__":
    main()
