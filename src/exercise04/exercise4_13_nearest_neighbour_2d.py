def find_nearest_neighbour_2d(points, target):
    if not points:
        raise ValueError("The list of points cannot be empty.")
    
    min_distance = float('inf')
    nearest_point = None
    for point in points:
        distance = ((point[0] - target[0]) ** 2 + (point[1] - target[1]) ** 2) ** 0.5
        if distance < min_distance:
            min_distance = distance
            nearest_point = point
    return nearest_point

def main():
    print("This program finds the nearest neighbour to a target point from a list of 2D points.")
    points = [(1, 2), (3, 4), (6, 1)]
    target = (2, 3)
    nearest = find_nearest_neighbour_2d(points, target)
    print(f"The nearest neighbour to {target} in the list {points} is: {nearest}")

    points = [(0, 0), (5, 5), (2, 1)]
    target = (3, 3)
    nearest = find_nearest_neighbour_2d(points, target)
    print(f"The nearest neighbour to {target} in the list {points} is: {nearest}")

if __name__ == "__main__":
    main()
