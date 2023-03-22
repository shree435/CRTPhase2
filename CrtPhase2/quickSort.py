def quickSort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    leftArr=[i for i in arr[1:] if i<=pivot]
    rightArr = [i for i in arr[1:] if i > pivot]
    return quickSort(leftArr)+[pivot]+quickSort(rightArr)
arr=[30,20,50,40,10,20]
print(arr)
res=quickSort(arr)
print(res)