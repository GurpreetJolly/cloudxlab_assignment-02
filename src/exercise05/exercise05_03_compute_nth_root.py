def compute_nth_root(x, n, tolerance, verbose=False):
    """Computes the nth root of x using binary search."""
    if x < 0 and n % 2 == 0:
        raise ValueError("Cannot compute even root of a negative number.")
    if x == 0:
        return 0, True
    if x == 1 or x == -1:
        return x, True

    # Set lower and upper bounds for binary search
    if x > 0:
        lower = 0
        upper = 1 if x < 1 else x
    else:
        lower = -1 if x > -1 else x
        upper = 0

    counter = 0
    mid_power = 0
    max_iterations = 10000

    while abs(x - mid_power) > tolerance and counter < max_iterations:
        counter += 1
        if verbose:
            print(f"{counter}. Guessing between {lower} and {upper}")
        mid = (lower + upper) / 2.0
        mid_power = mid ** n
        if verbose:
            print(f"\tEstimated {n}th root of {x} is approximately {mid}")
        if mid_power < x:
            lower = mid
        else:
            upper = mid

    if counter >= max_iterations:
        raise ValueError(f"Failed to converge after {counter} iterations. Last guess was {mid} with power {mid_power}")

    return mid, True

def main():
    print("\nThis program computes the nth root of a number using binary search.")
    verbose = input("Do you want to see the step-by-step process? (y/n): ").strip().lower() == 'y'
    tolerance = 1e-4
    targets = [[16,2], [27,3], [81,4]]
    for target in targets:
        print(f"\nFinding the {target[1]}th root of {target[0]} with a tolerance of {tolerance}")
        try:
            res, converged = compute_nth_root(target[0], target[1], tolerance, verbose)
            if converged:
                print(f"{target[1]}th root of {target[0]} is approximately {res}")
            else:            
                print(f"Failed to compute {target[1]}th root of {target[0]} within tolerance. Best guess is {res}")
        except ValueError as e:
            print(f"Error computing {target[1]}th root of {target[0]}: {e}")
    return 0

if __name__ == "__main__":
    main()
