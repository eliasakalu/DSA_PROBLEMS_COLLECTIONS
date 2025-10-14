#Naive Approach: => Time Complexity: O(n)  Auxiliary Space: O(1)
def firstLastOccurence(arr,x):
    first=-1
    last=-1
    for i in range(len(arr)):
        if arr[i]!=x:
            continue
        if first==-1:
            first=i
        last=i
    return first,last

#Efficent Approach:=> Time Complexity: O(log n)  Auxiliary Space: O(log n) 
def  firstOccurenceEfficently(arr,x,s,e):
    if s>e:
        return -1
    mid=(s+e)//2
    if arr[mid]==x and (arr[mid]>arr[mid-1] or mid==0):
        return mid
    elif arr[mid]>x:
        return firstOccurenceEfficently(arr,x,s,mid-1)
    else:
        return firstOccurenceEfficently(arr,x,mid+1,e)
def  lastOccurenceEfficently(arr,x,s,e):
    if s>e:
        return -1
    mid=(s+e)//2
    if arr[mid]==x and (mid==len(arr)-1 or arr[mid]<arr[mid+1]):
        return mid
    elif arr[mid]>x:
        return lastOccurenceEfficently(arr,x,s,mid-1)
    else:
        return lastOccurenceEfficently(arr,x,mid+1,e)


if __name__=="__main__":
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    x = 8
     #🔍 Naive Result
    first, last = firstLastOccurence(arr, x)
    if (first, last) == (-1, -1):
        print("🔎 Element not found")
    elif last==-1:
        print("🔎 Doesn\'t have last occurence")
    else:
        print(f"📍 First Occurrence (Naive) at index: {first}")
        print(f"📍 Last Occurrence (Naive) at index: {last}")

    #⚡ Efficient Result
    first_e = firstOccurenceEfficently(arr, x, 0, len(arr) - 1)
    last_e = lastOccurenceEfficently(arr, x, 0, len(arr) - 1)
    if first_e == -1:
        print("🔎 Element not found (Efficient)")
    else:
        print(f"⚡ First Occurrence (Efficient) at index: {first_e}")
        print(f"⚡ Last Occurrence (Efficient) at index: {last_e}")

