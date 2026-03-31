n = int(input())

n_div_10 = n % 10 == 0 
n_div_5 = n % 5 == 0 and n % 10 != 0

if n_div_10:
    print("Divisible by 10")
elif n_div_5:
    print("Divisible by 5")
else:
    print("Not Divisible by 10 or 5")
