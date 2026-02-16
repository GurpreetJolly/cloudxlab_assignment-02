def euclidean_distance(p1, p2):
    return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5

def manhattan_distance(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

def find_nearest_neighbour(target, points, distance_func):
    min_distance = float('inf')
    min_distance_neighbour = None
    for pn in points:
        distance = distance_func(target, pn)
        if distance < min_distance:
            min_distance = distance
            min_distance_neighbour = pn
    return min_distance_neighbour

def main():
    print("\n*** Computes either Euclidian or Manhattan distance ***")

    print("\n*** Example 1 ***")
    target = [1, 2]
    points = [[3, 4], [2, 2], [0, 0]]
    distance = find_nearest_neighbour(target, points, euclidean_distance)
    print(f"Nearest neighbour of point {target} among {points} using Euclidean distance is {distance}")

    print("\n*** Example 2 ***")
    target = [1, 2, 3]
    points = [[5, 5, 5], [0, 0, 0], [2, 2, 2]]
    distance = find_nearest_neighbour(target, points, manhattan_distance)
    print(f"Nearest neighbour of point {target} among {points} using Manhattan distance is {distance}")

if __name__ == "__main__":
    main()
