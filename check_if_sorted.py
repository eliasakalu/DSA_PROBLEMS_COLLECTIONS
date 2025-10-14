# Time Complexity: O(n) | Auxiliary Space: O(1)

def isSorted(l):
    """
    🔍 isSorted(l)
    Returns True if the list is sorted in ascending order.
    """
    if len(l) == 0:
        return True
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            return False
    return True

# 🧪 Driver Code
if __name__ == "__main__":
    List = [1, 2, 3, 4, 5]
    print("Sorted?: ", isSorted(List))