D = int(input()) # 125

bonus = 30
if D < 20:
    score = (D * 2) + bonus
elif D < 60:
    score = (20 * 2) + ((D - 20) *  4) + bonus
else:
    score = (20 * 2) + (40 * 4) + ((D - 60) * 6) + bonus
print(score)    
