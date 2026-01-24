import logging

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

def is_point_inside_rectangle(bottom_left_x:float, bottom_left_y:float, 
                              top_right_x:float, top_right_y:float, 
                              point_x:float, point_y:float) -> bool:
    inside = bottom_left_x <= point_x <= top_right_x and bottom_left_y <= point_y <= top_right_y
    _logger.debug(f"Point ({point_x}, {point_y}) inside rectangle "
                 f"(({bottom_left_x}, {bottom_left_y}), ({top_right_x}, {top_right_y})): {inside}")
    return inside

def main():
    print ("\n*** Check if point is inside rectangle ***")
    bottom_left_x = float(input("Enter bottom left x: "))
    bottom_left_y = float(input("Enter bottom left y: "))
    top_right_x = float(input("Enter top right x: "))
    top_right_y = float(input("Enter top right y: "))
    point_x = float(input("Enter point x: "))
    point_y = float(input("Enter point y: "))
    is_inside = is_point_inside_rectangle(bottom_left_x, bottom_left_y, top_right_x, top_right_y, point_x, point_y)
    print(f"Point ({point_x}, {point_y}) is {'inside' if is_inside else 'outside'} the rectangle.")
    print(is_inside)

if __name__ == "__main__":
    main()
