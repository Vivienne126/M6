#Part 2: The drag of negatives: running sum with reset

nums=[1,2,-5,0,4,3,6,]
print("Running sum trace")
running=0
for num in nums:
    running+=num
    if running<0:
        print(f"{num} sum {running}")
        running=0
    else:
        print(f"{num} sum : {running}")

print()
