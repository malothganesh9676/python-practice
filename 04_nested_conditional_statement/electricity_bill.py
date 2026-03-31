unit = int(input())

if unit <= 50:
    bill = unit * 2
elif unit <= 150:
    bill = (2 * 50) + (3 * (unit - 50))
elif unit <= 250:
    bill = (2 * 50) + (3 * 100) + (5 * (unit - 150))
else:
    bill = (2 * 50) + (3 * 100) + (5 * 100) + (8 * (unit - 250))
total = 0.2 * bill 
surcharge = total + bill 
print(surcharge)
