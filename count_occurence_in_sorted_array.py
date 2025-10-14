'''
Count Occurrences in Sorted Array

comments
Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[]. Expected time complexity is O(logn) 

Examples: 

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 2
  Output: 4 // x (or 2) occurs 4 times in arr[]

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 3
  Output: 1 

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 1
  Output: 2 

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 4
  Output: -1 // 4 doesn't occur in arr[] 

'''
#Naive Approach:=> Time Complexity: O(n)  Auxiliary Space: O(1)
#We just import our functions not built in function.
#These function are inside index_of_first_and_last_occurence.py file
from index_of_first_and_last_occurence import firstOccurenceEfficently, lastOccurenceEfficently

def count_occurrences(arr,x):
    n=len(arr)
    first=firstOccurenceEfficently(arr,x,0,n-1)
    last=lastOccurenceEfficently(arr,x,0,n-1)
    return (last-first+1)
if __name__ == "__main__":
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    x = 2
    c = count_occurrences(arr, x)
    print(f"The occurence of {x} in array:{c} times")