#Reverse in groups:
scores=[1,2,3,4,5,6,7,8]
n,i=3,0

while i<len(scores):
    start,end=i,min(i+n-1,len(scores)-1)
    while start<end:
        scores[start],scores[end]=scores[end],scores[start]
        start=start+1
        end=end-1
    i=i+n

print(f"Reversed in groups of 3 {scores}")
print()