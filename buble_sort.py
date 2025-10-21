# Bubble Sort (Naive): => Time Complexity: O(n^2) | Space Complexity: O(1)
def naiveBubbleSort(l):
    n = len(l)
    for i in range(n - 1):
        swapped=False
        for j in range(n - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped=True
        if swapped==False:
            return

if __name__ == "__main__":
    arr = [20, 1, 10, 3, 5, 2, 13]
    print(f"Before Sorting: {arr}")
    naiveBubbleSort(arr)
    print(f"After Sorting:  {arr}")