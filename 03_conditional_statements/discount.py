a = input()
b = input()

first_three_char = a[:3] == "DIS"
second_three_char = b[:3] == "DIS"

result = first_three_char or second_three_char
if result:
    print("Discount")
else:
    print("No Discount")
    
