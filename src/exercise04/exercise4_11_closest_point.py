def distance(p, a) -> float:
    """Calculate the Euclidean distance between points p and a."""
    squared_sum = 0
    for pn, an in zip(p, a):
        squared_sum += (pn - an) ** 2

    return squared_sum ** 0.5

def closer_point(p, a, b) -> str:
    """Return the point (a or b) that is closer to point p."""
    print (f"distance(p, a) = {distance(p, a)}")
    print (f"distance(p, b) = {distance(p, b)}")
    if distance(p, a) < distance(p, b):
        return 'A'
    elif distance(p, a) == distance(p, b):
        return 'Equal'
    else:
        return 'B'

def main():
    print("This program determines which of two points A or B is closer to point P.")
    print("Some example points are:")
    p = [1, 2]
    a = [0, 0]
    b = [5, 5]
    print()
    result = closer_point(p, a, b)
    print(f"The closer point to {p} between A={a} and B={b} is: {result}")

    p = [3, 3, 3]
    a = [0, 0, 0]
    b = [6, 6, 6]
    print()
    result = closer_point(p, a, b)
    print(f"The closer point to {p} between A={a} and B={b} is: {result}")

    p = [10, 10]
    a = [2, 2]
    b = [20, 20]
    print()
    result = closer_point(p, a, b)
    print(f"The closer point to {p} between A={a} and B={b} is: {result}")

if __name__ == "__main__":
    main()
