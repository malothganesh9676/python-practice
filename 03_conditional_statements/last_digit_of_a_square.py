n = input() # 15

square_n = str(int(n) ** 2)
last_digit_n = n[-1]
last_digit_square = square_n[-1]
result = last_digit_n == last_digit_square

if result:
    print("Equal")
else:
    print("Not Equal")
