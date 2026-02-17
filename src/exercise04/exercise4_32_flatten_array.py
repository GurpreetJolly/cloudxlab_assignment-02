def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            res = flatten_list(item)
            flat_list.extend(res)  # Recursively flatten the sublist
        else:
            flat_list.append(item)  # Append non-list items directly
    return flat_list

def main():
    print("\nFlatten Nested List Example")
    print("---------------------------")

    in_list = [1, [1, 2, [3, 4]]]
    print(f"\nExample 1: Flatten list {in_list}")
    result = flatten_list(in_list)
    print("Flattened list:", result)

    in_list = [1, [2, [3, [4, 5]]]]
    print(f"\nExample 2: Flatten list {in_list}")
    result = flatten_list(in_list)
    print("Flattened list:", result)

if __name__ == "__main__":
    main()
