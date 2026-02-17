
def is_point_on_line_1d(a: float, b: float, p: float) -> bool:
    if a < b:
        lower = a
        upper = b
    else:
        lower = b
        upper = a

    if lower <= p <= upper:
        return True
    return False

def main():
    print ("\n*** Check if given point is on line segment ***")
    a = float(input("Enter point a: "))
    b = float(input("Enter point b: "))
    p = float(input("Enter point p: "))
    is_on_line = is_point_on_line_1d(a, b, p)
    print(f"Point {p} is {'on' if is_on_line else 'not on'} the line segment between {a} and {b}.")
    print(is_on_line)

if __name__ == "__main__":
    main()
