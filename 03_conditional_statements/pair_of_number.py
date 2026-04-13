a = int(input())
b = int(input())

is_div_3 = a % 3 == 0 and b % 3 == 0 
is_div_12 = a % 12 == 0 or b % 12 == 0 

result = is_div_3 and is_div_12
if result:
    print("Pair")
else:
    print("Not a Pair")
