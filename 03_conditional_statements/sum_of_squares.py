a = int(input()) # 10
b = int(input()) # 2

a_square = a ** 2
b_square = b ** 2 

sum_square = a_square + b_square
is_greater_than = sum_square >= 60

if is_greater_than:
    print("Greater than or Equal to 60")
else:
    print("Less than 60")
