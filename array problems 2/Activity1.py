#Array problems 2

#Part 1 : Stock buy sell

prices=[100,180,260,310,40,535,695]
profit=0

for i in range(1,len(prices)):
    if prices[i]>prices[i-1]:
        profit=profit+prices[i]-prices[i-1]
print("Stock prices:" , prices)
print("Maximum Profit:" , profit)

#Part 2:Left tallest bar

heights=[0,1,2,1,0,3,4,2,1,4]
n=len(heights)
left_tallest=[0]*n
left_tallest[0]=heights[0]

for i in range(1,n):
    left_tallest[i]=max(left_tallest[i-1],heights[i])
print("Heights" , heights)
print("ledt talles:" , left_tallest)
print()

#Part 3: Right tallest bars

right_tallest=[0]*n
right_tallest[n-1]=heights[n-1]
for i in range(1,n):
    right_tallest[i]=max(right_tallest[i+1],heights[i])
print("Right tallest" , right_tallest)

#Part 4 rain water trapped

water=0
for i in range(n):
    water=water+min(left_tallest[i],right_tallest[i]-heights[i])
print("Total water trapped:" , water)