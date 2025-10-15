'''
Count 1's in a Sorted Binary List

comments
Given a binary array arr[] of size N, which is sorted in non-increasing order, count the number of 1's in it. 

Examples: 

Input: arr[] = {1, 1, 0, 0, 0, 0, 0}
Output: 2

Input: arr[] = {1, 1, 1, 1, 1, 1, 1}
Output: 7

Input: arr[] = {0, 0, 0, 0, 0, 0, 0}
Output: 0
'''
#Naive Approach:=> Time Complexity: O(n)  Auxiliary Space: O(1)
def countOnes(arr):
    count=0
    for i in range(len(arr)):
        if arr[i]==1:
            count+=1
    return count
#Efficent Approach:=> Time Complexity: O(logn) Auxilary Space: O(1)
from index_of_first_and_last_occurence import firstOccurenceEfficently,lastOccurenceEfficently
def countOnesEfficently(arr):
    firstoccured=firstOccurenceEfficently(arr,1,0,len(arr)-1) # to get the first index where 1 occured and its custom function build by mine you can check it inside index_of_first_and_last_occurence.py inside this repo
    lastoccured=lastOccurenceEfficently(arr,1,0,len(arr)-1) #to get the last index occurence of 1
    if (firstoccured,lastoccured)==(-1,-1):
        return 0
    elif lastoccured==-1:
        return 1
    return lastoccured-firstoccured+1

if __name__=="__main__":
    arr2 = [1, 1, 1, 1, 0, 0, 0]
    arr=[0,0,0]
    print(f"Using Naive Approach, The ammount of 1 in the array: {countOnes(sorted(arr))}")
    print(f"Using Efficent Approach, The ammount of 1 in the array: {countOnesEfficently(sorted(arr))}")