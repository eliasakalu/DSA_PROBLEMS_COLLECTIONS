# Naive Approach => Time Complexity: O((m+n) log (m+n)), Space Complexity: O(m+n)
def naiveMerge(arr, arr2):
    arr3 = arr + arr2
    arr3.sort()
    return arr3

# Efficient Approach => Time Complexity: O(m * n), Space Complexity: O(1)
def efficientMerge(arr, arr2):
    m = len(arr)
    n = len(arr2)

    for i in range(n - 1, -1, -1):
        last = arr[-1]
        j = m - 2

        # Shift elements in arr[] to the right if they are greater than arr2[i]
        while j >= 0 and arr[j] > arr2[i]:
            arr[j + 1] = arr[j]
            j -= 1

        # If any element was moved or last > arr2[i], swap
        if j != m - 2 or last > arr2[i]:
            arr[j + 1] = arr2[i]
            arr2[i] = last

    return arr + arr2

# Merge Function (Extra Space) => Time Complexity: O(m + n), Space Complexity: O(m + n)
def merge(arr, arr2):
    res = []
    m = len(arr)
    n = len(arr2)
    i = j = 0

    # Merge both arrays into res[]
    while i < m and j < n:
        if arr[i] < arr2[j]:
            res.append(arr[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    # Append remaining elements
    while i < m:
        res.append(arr[i])
        i += 1
    while j < n:
        res.append(arr2[j])
        j += 1

    return res

# Driver Code
if __name__ == "__main__":
    l = [1, 5, 9]
    l2 = [2, 13]

    print(f"Sorted array using naive approach     => {naiveMerge(l, l2)}")
    print(f"Sorted array using efficient approach => {efficientMerge(l, l2)}")
    print(f"Sorted array using merge() function   => {merge(l, l2)}")