def interpolationSearch(arr,left,right,x):
    if left<=right and x>=arr[left] and x<=arr[right]:
        pos=left+(((right-left)*(x-arr[left]))//(arr[right]-arr[left]))
        if arr[pos]==x:
            return pos
        elif arr[pos]<x:
            return interpolationSearch(arr,pos+1,right,x)
        else:
            return interpolationSearch(arr,left,pos-1,x)
    return -1

# Example usage:
arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
target = 19
index = interpolationSearch(arr, 0, len(arr) - 1, target)
if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")