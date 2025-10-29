'''
A sample sorted array for your assignment. You can use it to practice and compare linear search, binary search, jump search, and interpolation search step-by-step.

Assignment Array
python
arr = [5, 12, 18, 21, 25, 31, 36, 43, 47, 53, 59, 62, 70, 71, 83, 89, 95]'''

''' Find the number 47'''
 #Method 1: Linear Search
def linearSearch(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return f"{x} was found at index{i}."
    
    return -1
#Method 2: Jump Search
import math
def jumpSearch(arr,target):
    n=len(arr)
    step=int(math.sqrt(n))
    i=0
    while i<n and arr[min(step,n)-1]<target:
        i=step
        step+=int(math.sqrt(n))
        if i>=n:
            return -1
    while i<min(step,n):
        if arr[i]==target:
            return f"{target} was found at index {i}."
        elif arr[i]>target:
            break
        i+=1
    return -1
#Method 3: Binary Search
def binarySearch(arr,x):
    s=0
    e=len(arr)-1
    while s<=e:
        mid=(s+e)//2
        if arr[mid]==x:
            return f"{x} was found at index {mid}."
        elif arr[mid]>x:
            e=mid-1
        else:
            s=mid+1
    return -1
#Method 4: Interpolation
def interPolation(arr,x):
    low=0
    high=len(arr)-1
    while low<=high and arr[low]<=x<=arr[high]:
        pos=low+((high-low)*(x-arr[low]))//(arr[high]-arr[low])
        if arr[pos]==x:
            return f"{x} was found at index{pos}."
        elif arr[pos]<x:
            low=pos+1
        else:
            high=pos-1
    return -1


if __name__=="__main__":
    arr=[5, 12, 18, 21, 25, 31, 36, 43, 47, 53, 59, 62, 70, 71, 83, 89, 95]
    x=int(input("Enter Integer You Want To Search: "))
    print("Using Linear Search:", linearSearch(arr, x))
    print("Using Jump Search:", jumpSearch(arr, x))
    print("Using Binary Search:", binarySearch(arr, x))
    print("Using Interpolation Search:", interPolation(arr, x))

 