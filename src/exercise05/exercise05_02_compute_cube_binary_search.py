import sys

def cuberoot_binary_search (target:float, tolerance:float, verbose=False) -> tuple[float, bool]:
    """Computes an estimate of the cube root of a number."""
    if target == 0:
        return 0, True
    if target == 1 or target == -1:
        return target, True

    # Set lower and upper bounds for binary search
    if target > 0:
        lower = 0
        upper = 1 if target < 1 and target > 0 else target
    else:
        lower = -1 if target > -1 and target < 0 else target
        upper = 0

    counter = 0
    mid_cube = 0
    max_iterations = 10000

    while abs(target-mid_cube) > tolerance and counter < max_iterations:
        counter += 1
        if verbose:
            print (f"{counter}. Guessing between {lower} and {upper}")
        mid = (lower + upper) / 2.0
        mid_cube = mid * mid * mid
        if verbose:
            print(f"\tEstimated cube root of {target} is approximately {mid}")
        if mid_cube < target:
            lower = mid
        else:
            upper = mid

    if counter >= max_iterations:
        raise ValueError(f"Failed to converge after {counter} iterations. Last guess was {mid} with cube {mid_cube}")

    return mid, True

###################################
# Start of main program logic
##################################
def main():
    print("\nThis program computes the cube root of a number using binary search.")
    verbose = input("Do you want to see the step-by-step process? (y/n): ").strip().lower() == 'y'
    tolerance = 1e-4
    targets = [27, 8, -64, 0.001]
    for target in targets:
        print(f"\nFinding the cube root of {target} with a tolerance of {tolerance}")
        try:
            res, converged = cuberoot_binary_search(target, tolerance, verbose)
            if converged:
                print(f"Cube root of {target} is approximately {res}")
            else:            
                print(f"Failed to compute cube root of {target} within tolerance. Best guess is {res}")
        except ValueError as e:
            print(f"Error computing cube root of {target}: {e}")
    return 0

if __name__ == "__main__":
    main()
