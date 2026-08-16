#Array problems 3

#Part 1 : Streak counter reset

binary=[1,1,0,0,1,0,1,1,1,1]
streak=0
for num in binary:
    if num==0:
        streak=0
    else:
        streak+=1
    print(num,"->" , streak)
print()

#Part 2: Best streak tracker
streak=0
best=0
for num in binary:
    if num==0:
        streak=0
    else:
        streak+=1
        if streak>best:
            best=streak

print("Binary array:" , binary)
print("Max consequetive 1s:" , best)
print()

#Part 3:Same direction two pointers

nums=[1,0,3,6,0,0,0,2,355,0,72]
print("Before" , nums)
zero=0
for nonzero in range(len(nums)):
    if nums[nonzero]!=0:
        nums[nonzero],nums[zero]=nums[zero],nums[nonzero]
        zero=zero+1

print("After:" , nums)
print()

#Part 4:
print("Write pointer stopped at:" , zero)
print("Non zeros at front" , zero)
print("Zeros at end" , len(nums)-zero)