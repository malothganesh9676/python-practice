n = input() # 1634

first_digit_n = int(n[0]) ** 4
second_digit_n = int(n[1]) ** 4
third_digit_n = int(n[2]) ** 4 
last_digit_n = int(n[-1]) ** 4 

sum_power_n = first_digit_n + second_digit_n + third_digit_n + last_digit_n

result = sum_power_n == int(n)
if result:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
