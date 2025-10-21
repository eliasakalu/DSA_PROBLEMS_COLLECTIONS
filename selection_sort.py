def selectionSort(l):
    n=len(l)
    for i in range(n-1):
        index=i
        for j in range(i+1,n):
            if l[j]<l[index]:
                index=j
        l[index],l[i]=l[i],l[index]

l = [10, 5, 8, 20, 2, 18]
selectionSort(l)
print(f"The sorted array is ",*l)