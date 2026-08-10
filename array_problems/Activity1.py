#Two pointer swap

scores=[10,20,30,40,50]

start,end=0,len(scores)-1
while start<end:
    scores[start],scores[end]=scores[end],scores[start]
    start=start+1
    end=end-1

print(f"Swapped:{scores}")
print()