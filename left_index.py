'''
Left Index
Difficulty: EasyAccuracy: 57.84%Submissions: 8K+Points: 2Average Time: 10m
Given a sorted array of integers of size N and a number X. Find the leftmost index of X in the array arr[].

Example 1:

Input:
N = 10
arr[] = {1, 1, 2, 2, 3, 4, 5, 5, 6, 7}
X = 1
Output: 0 
Explanation: Because the element 1   
appears twice and its left most 
occurrence is at index 0.

Example 2:

Input:
N = 5
arr[] = {2, 2, 3, 3, 4}
X = 4
Output: 4
Explanation: Because element 4 appears 
only once at index 4.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function leftIndex() which takes the array arr[], its size N and an integer X as input parameters and returns the leftmost occurrence of X in arr[]. If X is not present in the array, return -1.

Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 106
-105 <= arr[i] <= 105
'''
def leftIndex (N, arr, X):
        s=0
        e=N-1
        while s<=e:
            mid=(s+e)//2
            if arr[mid]==X and (mid==0 or arr[mid]>arr[mid-1]):
                return mid
            elif arr[mid]<X:
                s=mid+1
            else:
                e=mid-1
        return -1

arr=[1,2,3,4,5,6]
k=6
print(f"The left most number {k} is located in index: {leftIndex(len(arr),arr,k)}")