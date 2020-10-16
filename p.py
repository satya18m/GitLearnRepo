def partition(arr,l,r):
    p=arr[l]
    j=l
    for x in range(l+1,r):
        if arr[x]<=p:
            j=j+1
            arr[j],arr[x]=arr[x],arr[j]
    arr[l],arr[j]=arr[j],arr[l]
    return j
def quicksort(arr,l,r):
    if l>=r:
        return
    m=partition(arr,l,r)
    quicksort(arr,l,m-1)
    quicksort(arr,m+1,r)
arr=[int(x) for x in input().split()]
quicksort(arr,0,len(arr))
print(arr)
