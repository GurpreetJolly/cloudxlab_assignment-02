import logging

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

def are_lines_touching_or_overlapping(l1x1:float, l1x2:float, l2x1:float, l2x2:float) -> bool:
    _logger.debug(f"Checking if lines are touching or overlapping.")
    if l1x1 > l1x2:
        l1lower = l1x2
        l1upper = l1x1
    else:
        l1lower = l1x1
        l1upper = l1x2
    if l2x1 > l2x2:
        l2lower = l2x2
        l2upper = l2x1
    else:
        l2lower = l2x1
        l2upper = l2x2
    _logger.debug(f"Line 1 range: [{l1lower}, {l1upper}]")
    _logger.debug(f"Line 2 range: [{l2lower}, {l2upper}]")
    if l1upper < l2lower or l2upper < l1lower:
        _logger.debug("Lines are not touching or overlapping.")
        return False
    return True

def main():
    print ("\n*** Check lines touching or overlapping ***")
    l1x1 = float(input("Enter x1 for line 1: "))
    l1x2 = float(input("Enter x2 for line 1: "))
    l2x1 = float(input("Enter x1 for line 2: "))
    l2x2 = float(input("Enter x2 for line 2: "))
    is_overlapping = are_lines_touching_or_overlapping(l1x1, l1x2, l2x1, l2x2)
    print(f"Lines are {'touching or overlapping' if is_overlapping else 'not touching or overlapping'}.")
    print(is_overlapping)

if __name__ == "__main__":
    main()
