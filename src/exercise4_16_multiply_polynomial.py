def multiply_polynomial(poly, num):
    for i in range(len(poly)):
        poly[i] = num * poly[i]
    return poly

def main():
    print("\n*** Multiplies number with polynomial ***")

    print("\n*** Example 1 ***")
    num = 5
    poly = [2, 0, 3, 10]
    print(f"Result of polynomial {poly} multiply by {num} is -")
    m_poly = multiply_polynomial(poly, num)
    print(f"{m_poly}")
    
    print("\n*** Example 2 ***")
    num = 3
    poly = [1, -2, 4]
    print(f"Result of polynomial {poly} multiply by {num} is -")
    m_poly = multiply_polynomial(poly, num)
    print(f"{m_poly}")
    
if __name__ == "__main__":
    main()
