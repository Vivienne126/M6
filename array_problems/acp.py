print("ROTATE SCORES")

#Two pointer swap

scores=[1,2,3,4,5,6]
start=scores[0]
end=scores[len(scores)-1]

while start<end:
    scores[start],scores[end]=scores[end],scores[start]
    start+=1
    end-=1

print(f"SCORES: {scores}")
print(f"SWAPPED: ")