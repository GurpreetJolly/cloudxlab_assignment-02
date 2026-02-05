def add_polynomials(p1, p2):
    if len(p1) != len(p2):
        raise ValueError("Length of both polynomials should be same")

    sum_poly = []
    for i in range(len(p1)):
        sum_poly[i] = p1[i] + p2[i]

    return sum_poly

def main():
    print("\nAdds to polynomials to create new polynomial")

    print("\n*** Example 1 ***")
    p1 = [2, 0, 3, 10]
    p2 = [1, 4, 0, 6]
    print(f"Addition of polynomial {p1} and {p2} = {add_polynomials(p1, p2)}")

    print("\n*** Example 2 ***")
    p1 = [5, 2] 
    p2 = [3]
    print(f"Addition of polynomial {p1} and {p2} = {add_polynomials(p1, p2)}")