#Leaders in a list

scores=[20,17,8,5,2,3,2]
max_right=scores[-1]
leaders=[max_right]

for i in range(len(scores)-2,-1,-1):
    if scores[i]>max_right:
        max_right=scores[i]
        leaders.append(scores[i])

leaders.reverse()
print(f"Scores: {scores}")
print(f"Leaders: {leaders}")
