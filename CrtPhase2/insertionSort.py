def insertionSort(arr):
    for i in range (1,len(arr)):
        temp=i
        while arr[temp-1]>arr[temp] and temp>0:
            arr[temp-1],arr[temp]=arr[temp],arr[temp-1]
            temp-=1
    return arr
arr=[2,17,5,13,23,21,8]
print(arr)
print(insertionSort(arr))