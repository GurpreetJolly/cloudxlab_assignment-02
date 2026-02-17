def find_nearest_neighbour(numbers, target):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    
    min_distance = int(1e10)
    min_distance_number = None
    for i in range(len(numbers)):
        if abs(numbers[i] - target) < min_distance:
            min_distance = abs(numbers[i] - target)
            min_distance_number = numbers[i]
    return min_distance_number

def main():
    print("This program finds the nearest neighbour to a target number from a list of numbers.")
    numbers = [2, 5, 8, 12]
    target = 6
    nearest = find_nearest_neighbour(numbers, target)
    print(f"The nearest neighbour to {target} in the list {numbers} is: {nearest}")

    numbers = [1, 4, 10, 20]
    target = 15
    nearest = find_nearest_neighbour(numbers, target)
    print(f"The nearest neighbour to {target} in the list {numbers} is: {nearest}")

if __name__ == "__main__":
    main()

