def merge(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    i = j = 0
    k = l
    len_left = len(left)
    len_right = len(right)

    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            k+=1
        else:
            arr[k] = right[j]
            j += 1
            k += 1

    while i < len_left:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len_right:
        arr[k] = right[j]
        j += 1
        k += 1

def mergesort(arr,l,r):
    if r>l:
        m=(r+l)//2
        mergesort(arr,l,m)
        mergesort(arr,m+1,r)
        merge(arr,l,m,r)
    return arr

arr=[57,6,6,7,3,1,12,100]
print(*mergesort(arr,0,len(arr)-1))
