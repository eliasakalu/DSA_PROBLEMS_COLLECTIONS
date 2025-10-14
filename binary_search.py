'''
Binary Search
Problem: Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

Examples:  

Input: arr[] = {10, 20, 30, 50, 60, 80, 110, 130, 140, 170}, x = 110
Output: 6
Explanation: Element x is present at index 6

Input: arr[] = {10, 20, 30, 40, 60, 110, 120, 130, 170}, x = 175
Output: -1
Explanation: Element x is not present in arr[].
'''

def binarySearch(array,x):
    s=0
    e=len(array)-1
    while s<=e:
        mid=(s+e)//2
        if array[mid]==x:
            return f"{x} was found at index:{mid}"
        elif array[mid]<x:
            s=mid+1
        else:
            e=mid-1
    return f"{x} was not found!"

if __name__=="__main__":
    array=[2,5,12,16,23,38,56,72,91]
    print(binarySearch(array,12))