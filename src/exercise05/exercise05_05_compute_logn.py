def log_base_n(x, n, tolerance, verbose=False) -> tuple[float, bool]:
    if x <= 0:
        raise ValueError("Input must be a positive integer.")
    if n <= 1:
        raise ValueError("Base must be a positive integer not equal to 1.")
    
    counter = 0
    mid_logn = 0
    max_iterations = 10000

    lower = 0 if x >= 1 else -100   # -100 is an arbitrary choice.
    upper = max(1, x/n+1)   # This is done to handle larger numbers else it overflows very soon.
    
    while abs(x - mid_logn) > tolerance and counter < max_iterations:
        counter += 1
        if verbose:
            print(f"{counter}. Guessing between {lower} and {upper}")
        mid = (lower + upper) / 2.0
        mid_logn = n**mid
        if verbose:
            print(f"\tEstimated log_{n} of {x} is approximately {mid}")
        if mid_logn < x:
            lower = mid
        else:
            upper = mid

    if counter >= max_iterations:
        raise ValueError(f"Failed to converge after {counter} iterations. Last guess was {mid} with power {mid_logn}")
    return mid, True


###################################
# Start of main program logic
##################################
def main():
    print("\n*** Computes the logn of a number using binary search. ***")
    tolerance = 1e-7    # Accuracy of result is pre-defined here. More precision will require more iterations to converge.
    verbose = input("Do you want to see the step-by-step process? (y/n): ").strip().lower() == 'y'
    tolerance = 1e-4
    targets = [[8,2], [81,3], [0.04,5], [10,2], [100,100]]

    for target in targets:    
        print(f"\nFinding log_{target[1]} of {target[0]} with a tolerance of {tolerance}")
        try:
            if isinstance(target, list):
                result,converged = log_base_n(target[0], target[1], tolerance, verbose)
            else:
                result,converged = log_base_n(target, 10, tolerance, verbose)
            if converged:
                print(f"Result: {result}")
            else:
                print(f"Failed to converge for target {target}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    return 0

if __name__ == "__main__":
    main()
