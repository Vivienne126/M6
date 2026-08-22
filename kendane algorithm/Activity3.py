#Part 3: Max so far : capture the best before reset erases it
nums=[1,2,-5,0,4,3,6,]
running=0
best=0
for num in nums:
    running+=nums
    if running<0:
        running=0
    if running>best:
        best=running
print("Array" , nums)
print("Max Subarray sum:" , best)
print()