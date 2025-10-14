'''
Given a sorted array, the task is to remove the duplicate elements from the array and return its size of reduced array.
Examples: 

Input  : arr[] = {2, 2, 2, 2, 2}
Output : 1

Input  : arr[] = {1, 2, 2, 3, 4, 4, 4, 5, 5}
Output : 5  

'''
#Naive Approach => Time Complexity : O(n)   Auxiliary Space : O(n)
def removeDuplicates(arr,n):
    temp=[0]*n
    temp[0]=arr[0]
    res=1

    for i in range(1,n):
        if temp[res-1]!=arr[i]:
            temp[res]=arr[i]
            res+=1
    
    for i in range(res):
        arr[i]=temp[i]

    return res
#Efficent Approach: => Time Complexity : O(n)  Auxiliary Space : O(1)
def removeDuplicates_2(arr,n):
    res=1
    for i in range(1,n):
        if arr[res-1]!=arr[i]:
            arr[res]=arr[i]
            print(arr)
            res+=1
    return res

n = 7  # Size of the array
arr = [10, 20, 20, 30, 30, 70, 30]
print(removeDuplicates(sorted(arr), n)) 
print(removeDuplicates_2(sorted(arr), n)) 