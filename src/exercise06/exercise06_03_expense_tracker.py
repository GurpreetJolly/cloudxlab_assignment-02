def update_expenses(expense_list:list[tuple], expenses_dict:dict):
    """
    Updates the dictionary with expenses from the list.
    Each element of expense_list is a tuple: (expense_head, amount).
    If the head already exists, add to its total.
    Otherwise, create a new entry.
    """
    for expense in expense_list:
        category = expense[0]
        amount = expense[1]
        if category in expenses_dict:
            expenses_dict[category] += amount
        else:
            expenses_dict[category] = amount

def print_expenses(expenses_dict):
    """
    Prints all expense heads and their total amounts.
    Example format:
    food : 500
    rent : 1000
    """
    print("List of Expense")
    for category, total in expenses_dict.items():
        print(f"{category:10s}: {total:10.2f}")

def main():
    print("\n*** Expense Tracker ***")
    expenses = {}
   
    expense_list1 = [('food', 200), ('rent', 1000)]
    expense_list2 = [("food", 300), ("travel", 150)]
    
    print(f"Updating expenses with first list {expense_list1}...")
    update_expenses(expense_list1, expenses)
    #print_expenses(expenses)
    
    print(f"Updating expenses with second list {expense_list2}...")
    update_expenses(expense_list2, expenses)
    print_expenses(expenses)

if __name__ == "__main__":
    main()
