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

#Reverse in groups:
scores=[1,2,3,4,5,6,7,8,9,10,422,12,18]
n,i=2,0

while i<len(scores):
    start,end=i,min(i+n-1,len(scores)-1)
    while start<end:
        scores[start],scores[end]=scores[end],scores[start]
        start=start+1
        end=end-1
    i=i+n

print(f"Reversed in groups of 2 {scores}")
print()

#Part 3: Left rotate by n
scores=[16,22,302,49,500]

for i in range(4):
    temp=scores[0]
    for i in range(1,len(scores)):
        scores[i-1]=scores[i]
    scores[-1]=temp

print(f"Rotated left by 4: {scores}")
print()

#Leaders in a list

scores=[20,17,8,5,2,3,2,12,32]
max_right=scores[-1]
leaders=[max_right]

for i in range(len(scores)-2,-1,-1):
    if scores[i]>max_right:
        max_right=scores[i]
        leaders.append(scores[i])

leaders.reverse()
print(f"Scores: {scores}")
print(f"Leaders: {leaders}")
