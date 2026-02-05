def find_nearest_neighbour_nd(points, target):
    if not points:
        raise ValueError("The list of points cannot be empty.")
    
    min_distance = float('inf')
    nearest_point = None
    for i in range(len(points)):
        if len(target) != len(points[i]):
            raise ValueError("All points and the target must have the same number of dimensions.")
        distance = 0
        for pn, tn in zip(points[i], target):
            distance += (pn - tn) ** 2
        distance = distance ** 0.5
        if distance < min_distance:
            min_distance = distance
            nearest_point = points[i]
    return nearest_point

def main():
    print("This program finds the nearest neighbour to a target point from a list of N-dimensional points.")
    print("Example with N-Dimensional points:")
    
    points = [[3, 4], [2, 1], [0, 0]]
    target = [1, 2]
    nearest = find_nearest_neighbour_nd(points, target)
    print(f"The nearest neighbour to {target} in the list {points} is: {nearest}")

    points = [[1, 1, 1], [2, 2, 2], [-1, -1, -1]]
    target = [0, 0, 0]
    nearest = find_nearest_neighbour_nd(points, target)
    print(f"The nearest neighbour to {target} in the list {points} is: {nearest}")

if __name__ == "__main__":
    main()
