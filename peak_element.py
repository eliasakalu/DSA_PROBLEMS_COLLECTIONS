#Naive Approach:=>
def isPeakExistSimply(arr):
    n=len(arr)
    if n==0:
        return -1 #Empty Array
    if n==1:
        return 0 #Single Array
    if arr[0]>arr[1]:
        return 0
    if  arr[-1]>arr[-2]:
        return n-1
    for i in range(1,n-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            return  i
    return -1
#Efficent Approach:=> Binary Approach
def isPeakExistEfficently(arr):
    n=len(arr)
    s=0
    e=n-1
    while s<=e:
        mid=(s+e)//2
        right=arr[mid+1] if mid<n-1 else float('-inf')
        left=arr[mid-1] if mid>0 else float('-inf')
        if arr[mid]>left and arr[mid]>right:
            return mid
        elif arr[mid]<right:
            s=mid+1
        else:
            e=mid-1
    return -1
arr=[5, 2 ,1]
x=isPeakExistSimply(arr) 
y=isPeakExistEfficently(arr) 
print("Peak Found" if x!=-1 else "Peak Not found")
print("Peak Found" if y!=-1 else "Peak Not found")

