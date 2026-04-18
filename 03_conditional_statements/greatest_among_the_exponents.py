a = int(input()) # 2
b = int(input()) # 3

a_power_b = a ** b 
b_power_a = b ** a 

is_greatest = b_power_a > a_power_b
if is_greatest:
    print(b_power_a)
else:
    print(a_power_b)
