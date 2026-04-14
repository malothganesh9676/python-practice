n = input() #371

first_digit_n = int(n[0]) ** 3
secong_digit_n = int(n[1]) ** 3
last_digit_n = int(n[-1]) ** 3

sum_of_n = first_digit_n + secong_digit_n + last_digit_n
result = int(n) == sum_of_n
if result:
    print("True")
else:
    print("False")
