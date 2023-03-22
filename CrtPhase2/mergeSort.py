def merge(arr,left,right,middle):
    leftArr=arr[left:middle]
    rightArr=arr[middle+1:right+1]
    leftIndex=0
    rightIndex=0
    index=left
    while leftIndex<len(leftArr) and rightIndex<len(rightArr):
        if leftArr[leftIndex]<=rightArr[rightIndex]:
            arr[index]=leftArr[leftIndex]
            leftIndex+=1
        else:
            arr[index]=rightArr[rightIndex]
            rightIndex+=1
        index+=1
    while leftIndex<len(leftArr):
        arr[index]=leftArr[leftIndex]
        leftIndex+=1
        index+=1
    while rightIndex<len(rightArr):
        arr[index]=rightArr[rightIndex]
        rightIndex+=1
        index+=1
def mergeSort(arr,left,right):
    if left>=right:
        return
    else:
        mid=(left+right)//2
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        merge(arr,left,right,mid)
arr=[5,8,1,9,7,4,6,3]
print(arr)
print(mergeSort(arr,0,len(arr)-1))