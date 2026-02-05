import exercise3_5_hcf as hcf

def eliminate_variable(eq1, eq2, var_index):
    ret = []
    if var_index >= len(eq1)-1:
        print(f"Error: Cannot solve for variable at location {var_index} because it is out of range")
    elif var_index >= len(eq2)-1:
        print(f"Error: Cannot solve for variable at location {var_index} because it is out of range")
    elif len(eq1) != len(eq2):
        print(f"Error: Cannot solve for equation {eq1} and {eq2} because the length is not same")
    else:
        eq1c = eq1[var_index]
        eq2c = eq2[var_index]
        #Multiply equation1 to make the coefficient to eliminate equal to equation2
        for i in range(len(eq1)):
            eq1[i] *= eq2c
        #Multiply equation2 to make the coefficient to eliminate equal to equation1
        for i in range(len(eq2)):
            eq2[i] *= eq1c
        #Subtract equation2 from equation1
        for i in range(len(eq1)):
            ret.append(eq1[i]-eq2[i])
        #Remove eliminated coefficient from final equation
        ret.remove(0)
        #If there is possibility of reducing coefficient the find HCF and divide by HCF
        ret_hcf = abs(ret[0])
        for i in range(len(ret)):
            ret_hcf = hcf.compute_hcf(ret_hcf, abs(ret[i]))
        for i in range(len(ret)):
            ret[i] //= ret_hcf
    return ret

def main():
    print("\n*** Eliminate a one variable and returns final equation ***")
    eq1 = [2, 3, 8]
    eq2 = [4, -1, 2]
    index_to_eliminate = 0
    print(f"\nEliminate variable at index {index_to_eliminate} from equations {eq1} and {eq2}")
    a_list = eliminate_variable(eq1, eq2, index_to_eliminate)
    print(f"Result: {a_list}")

    eq1 = [1, 2, 3]
    eq2 = [3, 1, 7]
    index_to_eliminate = 1
    print(f"\nEliminate variable at index {index_to_eliminate} from equations {eq1} and {eq2}")
    a_list = eliminate_variable(eq1, eq2, index_to_eliminate)
    print(f"Result: {a_list}")

if __name__ == "__main__":
    main()
