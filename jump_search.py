import math
def jumpSearch(arr,target):
    i=0
    n=len(arr)
    step=int(math.sqrt(n))
    while i<n and arr[min(i+step-1,n-1)]<target:
        i+=step
        if i>=n:
            return -1
    for j in range(i,min(i+step,n)):
        if arr[j]==target:
            return f"{target} was found at index {j}"
    return -1

# Example usage
if __name__ == "__main__":
    arr = [2, 5, 8, 13, 17, 24, 32, 39, 44, 55]
    target = 32
    result = jumpSearch(arr, target)
    if result != -1:
        print(f"Element {target} found at index: {result}")
    else:
        print(f"Element {target} not found in the array.")