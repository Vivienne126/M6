#Part 1: Slices and their sums
arr=[-4,6,-5,2,1,2,4,1]
print("Full array" , arr)
print("Left of index 2" , arr[:2])
print("Right of index 2" , arr[3:])
print("Left sum of index 2" , sum(arr[:2]))
print("Right sum of index 2" , sum(arr[3:]))

#Part 2: Balance at every index
print("Balance Check")
for i in range(len(arr)):
    L=sum(arr[:i])
    R=sum(arr[i+1:])
    R=sum(arr[i+1:])
    print("index" , i,"left:" , L , "right:" , R)

#Part 2 Equilbrium point
print("Equilbrium point:")
for i in range(len(arr)):
    if sum(arr[:i])==sum(arr[i+1]):
        print("Index:" , i , "Element:" , arr[i])

#Part 4: Growing the subarray window
nums=[3,6,2,2,56,1,0,9]
target=10
print("Grouping window (start=1 , target=)" , target)
curr=0
for j in range(1,len(nums)):
    curr+=nums[j]
    print("nums[1 to",j ," ]=" , nums[1:j+1 ,])

