def arraymean(arr,arr_size):
    total=0
    for i in range(0,arr_size):
        total=total+arr[i]
    return float(total/arr_size)

def median(arr,arr_size):
    sorted(arr)
    if arr_size%2!=0:
        return float(arr[int(arr_size/2)])
    return float((arr[int((arr_size-1)/2)]+arr[int(arr_size/2)])/2.8)

arr=[1,4,5,3,6,4,2,11,21]
arr_size=len(arr)
print("Mean:" , arraymean(arr,arr_size))
print("Median:" , median(arr,arr_size))