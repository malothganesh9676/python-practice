n = int(input())

divisible_5 = n % 5 == 0 and n % 7 == 0
is_less_than = n < 7 

result = divisible_5 or is_less_than
if result:
    print(n)
else:
    print(n % 5)
    print(n % 7)
