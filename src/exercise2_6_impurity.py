import random

def my_impurity_ratio(c1, c2):
    if c1 == 0 or c2 == 0:
        return 0.0
    else:
        if c1 < c2:
            return c1/c2
        else:
            return c2/c1

def my_impurity_ratio_total(c1, c2):
    total = c1 + c2
    if total == 0:
        return 0.0
    else:
        if c1 < c2:
            return 2*c1/total
        else:
            return 2*c2/total

def main():
    # Create 2 random numbers that signifies the count of class1 and class2
    print("\n *** This will generate two random counts for class c1 and c2 and compute their impurity. ***")
    print(" *** Impurity is defined as the ratio of the smaller count to the larger count. ***")
    print(" *** Alternatively, impurity can also be defined as twice the smaller count divided by the total count of both classes. ***")
    print(" *** If either count is zero, impurity is defined to be 0.0 ***")
    print(" *** If count for both classes c1 & c2 are same then impurity is 1.0 ***")
    i = "1"
    while i == "1":
        class1Count = random.randint(0, 1000)
        class2Count = random.randint(0, 1000)
        print (f"\nClass 1 Count: {class1Count}, Class 2 Count: {class2Count}")
        impurity_value_r = my_impurity_ratio(class1Count, class2Count)
        impurity_value_t = my_impurity_ratio_total(class1Count, class2Count)
        print(f"Impurity between class1 and class2 using ratios: {impurity_value_r}")
        print(f"Impurity between class1 and class2 using percentage of total count: {impurity_value_t}")
        i = input("Press 1 and <Enter> to compute another set of counts of class c1 and c2 and then compute their impurity...")
    
    print("\n*** Some more examples ***")
    print(f"my_impurity_ratio(0, 5)={my_impurity_ratio(0, 5)}\t# Expected output: 0.0")
    print(f"my_impurity_ratio(5, 5)={my_impurity_ratio(5, 5)}\t# Expected output: 1.0")

if __name__ == "__main__":
    main()
