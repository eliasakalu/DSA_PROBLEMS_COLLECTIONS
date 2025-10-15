'''
Count 1's in binary array
Difficulty: EasyAccuracy: 49.3%Submissions: 64K+Points: 2Average Time: 20m
You are given a binary array that is sorted in non-increasing order, meaning all the 1's appear before the 0's. Find the total number of 1's present in the array.

Examples:

Input: arr[] = [1, 1, 1, 1, 1, 0, 0, 0]
Output: 5
Explaination: Count of 1's in the array is 5.
Input: arr[] = [1, 1, 1, 1, 1, 1, 1]
Output: 7
Explaination: Count of 1's in the array is 7.
'''
def countOnes(arr):
    n=len(arr)
    s=0
    e=n-1
    while s<=e:
        mid=(s+e)//2
        if arr[mid]==1 and (arr[mid+1]<arr[mid] or mid==n-1):
            return mid+1
        elif arr[mid]<1:
            e=mid-1
        else:
            s=mid+1
    return 0
arr=[1,1,0,0,0]
print(f"Original array:{arr}")
print(f"The number of ones inside the array is:{countOnes(arr)}")