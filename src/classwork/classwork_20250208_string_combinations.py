####################
# Work in progress #
####################

from math import factorial

def FindCombinations(in_list) -> list:
    a_combination = []
    for i in range(factorial(len(in_list))):
        for j in range(len(in_list)):
            if in_list[j] not in a_combination: 
                a_combination.append(in_list[j])
            else:
                
            print(a_combination)
        print(a_combination)
    return True

def main():
    a_list = ['a', 'b', 'c']
    new_list = FindCombinations(a_list)