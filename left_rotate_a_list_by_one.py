"""
🔁 Left Rotation of an Array by One Element

If the input array is given, the rotation by one element is:
Input:
    [10, 20, 30, 40]
Output:
    [20, 30, 40, 10]
"""

# ✅ Method 1: Slicing Method
def rotate_to_left(arr, n):
    return arr[1:] + arr[:1]

# ✅ Method 2: Append-Pop Method
def rotate_to_left_2(arr, n):
    arr.append(arr.pop(0))
    return arr

# ✅ Method 3: Iterative Approach
def rotate_to_left_3(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(1, n):
        arr[i - 1] = arr[i]
    arr[n - 1] = temp
    return arr

# 🚀 Driver Code
if __name__ == "__main__":
    l = [10, 20, 30, 40]
    print(f"The list before rotation: {l}")
    
    # Using Method 1
    rotated_1 = rotate_to_left(l.copy(), len(l))
    print(f"After rotation (Slicing): {rotated_1}")
    
    # Using Method 3
    rotated_3 = rotate_to_left_3(l.copy())
    print(f"After rotation (Iterative): {rotated_3}")
    
    # Using Method 2
    rotated_2 = rotate_to_left_2(l.copy(), len(l))
    print(f"After rotation (Append-Pop): {rotated_2}")