def are_rectangles_intersecting(rect1: tuple, rect2: tuple) -> bool:
    # Unpack rectangle coordinates
    rect1_top_left = rect1[0]
    rect1_bottom_right = rect1[1]
    rect2_top_left = rect2[0]
    rect2_bottom_right = rect2[1]

    max_x = max(rect1_top_left[0], rect2_top_left[0])
    min_x = min(rect1_bottom_right[0], rect2_bottom_right[0])

    max_y = min(rect1_top_left[1], rect2_top_left[1])
    min_y = max(rect1_bottom_right[1], rect2_bottom_right[1])

    if max_x <= min_x and max_y <= min_y:
        return True
    else:
        return False


def main():
    rectangle1 = ((0, 0), (3, 3))
    rectangle2 = ((2, 2), (5, 5))
    is_intersecting = are_rectangles_intersecting(rectangle1, rectangle2)  # Output: True
    print(f"Rectangle1 {rectangle1} and Rectangle2 {rectangle2} intersect: {is_intersecting}")  # Expected: True

    # One rectangle is completely to the right of the other
    rectangle1 = ((0, 0), (1, 1))
    rectangle2 = ((2, 2), (3, 3))
    is_intersecting = are_rectangles_intersecting(rectangle1, rectangle2)  # Output: False
    print(f"Rectangle1 {rectangle1} and Rectangle2 {rectangle2} intersect: {is_intersecting}")  # Expected: False

    # Touching at corner
    rectangle1 = ((0, 0), (2, 2))
    rectangle2 = ((2, 2), (4, 4))
    is_intersecting = are_rectangles_intersecting(rectangle1, rectangle2)  # Output: True
    print(f"Rectangle1 {rectangle1} and Rectangle2 {rectangle2} intersect: {is_intersecting}")  # Expected: True

    # One rectangle inside another
    rectangle1 = ((0, 0), (5, 5))
    rectangle2 = ((1, 1), (2, 2))
    is_intersecting = are_rectangles_intersecting(rectangle1, rectangle2)  # Output: True
    print(f"Rectangle1 {rectangle1} and Rectangle2 {rectangle2} intersect: {is_intersecting}")  # Expected: True

    rectangle1 = ((1, 1), (4, 4))
    rectangle2 = ((2, 2), (5, 5))
    is_intersecting = are_rectangles_intersecting(rectangle1, rectangle2)  # Output: True
    print(f"Rectangle1 {rectangle1} and Rectangle2 {rectangle2} intersect: {is_intersecting}")  # Expected: True

    rectangle1 = ((1, 1), (4, 4))
    rectangle2 = ((5, 5), (6, 6))
    is_intersecting = are_rectangles_intersecting(rectangle1, rectangle2)  # Output: False
    print(f"Rectangle1 {rectangle1} and Rectangle2 {rectangle2} intersect: {is_intersecting}")  # Expected: False

if __name__ == "__main__":
    main()
