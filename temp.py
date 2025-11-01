def bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        sorted=False
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                sorted=True
        if sorted==False:
            return

def selectionsort(arr):
    for i in range(len(arr)-1):
        temp=i
        for j in range(1+i,len(arr)):
            if arr[temp]>arr[j]:
                temp=j
        arr[i],arr[temp]=arr[temp],arr[i]

def insertionSort(arr):
    for i in range(1,len(arr)):
        x=arr[i]
        j=i-1
        while j>=0 and x<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=x


arr=[20,45,2,3,12,32,1]
insertionSort(arr)
print(arr)
