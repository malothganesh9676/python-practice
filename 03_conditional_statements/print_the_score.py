distance = int(input())

if distance <= 10:
    score = distance
else:
    remaining_distance = distance - 10 
    score = 10 + (remaining_distance * 3)
print(score)    
