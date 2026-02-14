import exercise4_20_eliminate_one_variable_2Equations as le

xns = []

def find_xn(ret):
    b_sum = 0
    knowns_sum = 0
    unknowns_sum = 0
    for i in range(len(ret)):        # Horizontal flow
        b_sum += ret[i][len(ret[i])-1]  # could be ret[0] too
        unknowns_sum += ret[i][0]
        for j in range(1, len(ret[i])-1):  # Vertical flow
            knowns_sum += ret[i][j]*xns[len(xns)-j]
    xn = (b_sum - knowns_sum)/unknowns_sum
    xns.append(xn)
    
def solve_equations(equations) -> float:
    if len(equations) > 1:
        ret = []
        for i in range(len(equations)-1):
            a = list(equations[i])
            b = list(equations[i+1])
            print(f"{i}: {a}")
            print(f"{i+1}: {b}")
            reduced = le.eliminate_variable(equations[i], equations[i+1], 0)
            ret.append(reduced)
            print(f"{i}, {i+1} is reduced to {reduced}")
        if (len(ret) > 1):
            xn = solve_equations(ret)
        find_xn(ret)

def main():
    #equations = [[2, 1, 5], [1, -1, 1]]
    #equations = [[2, 1, 5, 1], [1, -1, 1, 1], [1, 1, 2, 5]]
    equations = [[1, 1, 1, 6], [0, 2, 5, -4], [2, 5, -1, 27]]
    solve_equations(equations)
    find_xn(equations)
    xns.reverse()
    print(f"xn={xns}")

if __name__ == "__main__":
    main()
