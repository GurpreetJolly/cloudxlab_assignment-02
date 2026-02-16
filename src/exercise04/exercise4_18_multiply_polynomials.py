def multiply_polynomials(p1: list, p2: list):
    p1.reverse()
    p2.reverse()

    res = []
    for i in range(len(p1) + len(p2) - 1):
        res.append(0)

    for i in range(len(p1)):
        for j in range(len(p2)):
            res[i+j] += p1[i]*p2[j]
    res.reverse()
    return res

def mp(p1: list, p2: list):
    res = []
    res_length = len(p1) + len(p2) - 1
    for i in range(res_length):
        res.append(0)

    for i in range(len(p1)):
        for j in range(len(p2)):
            res[res_length-1 - (i + j)] += p1[i]*p2[j]

    return res

def main():
    print("\n*** Multiply polynomials ***")
    print("\n*** Example 1 ***")
    p1 = [2, 3]
    p2 = [1, 4]
    print(f"Multiplication of polynomials {p1} and {p2} is -")
    print(f"Result using reversal: {multiply_polynomials(p1, p2)}")
    print(f"Result using without reversal {mp(p1, p2)}")

    print("\n*** Example 2 ***")
    p2 = [2, 0, 3, 10]
    p1 = [1,  2]
    print(f"Multiplication of polynomials {p1} and {p2} is -")
    print(f"Result using reversal: {multiply_polynomials(p1, p2)}")
    print(f"Result using without reversal {mp(p1, p2)}")

if __name__ == "__main__":
    main()
