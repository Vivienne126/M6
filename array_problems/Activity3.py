#Part 3: Left rotate by n
scores=[10,20,30,40,50]

for i in range(2):
    temp=scores[0]
    for i in range(1,len(scores)):
        scores[i-1]=scores[i]
    scores[-1]=temp

print(f"Rotated left by 2: {scores}")
print()