# Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(f"i = {i}, arr = {arr}")
        for j in range(n-1, i, -1):
            print(f"  j = {j}, comparing arr[{j}] = {arr[j]} and arr[{j-1}] = {arr[j-1]}")
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                print(f"    Swapped: arr = {arr}")
    return arr

def main():
    # Sample array to be sorted
    print("\n*** Bubble Sort Algorithm Example ***")
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
