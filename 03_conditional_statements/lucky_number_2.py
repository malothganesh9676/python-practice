n = input()

is_divisible_9 = int(n) % 9 == 0
is_one_of = int(n[0]) == 9 or int(n[1]) == 9 

result = is_divisible_9 or is_one_of
if result:
    print("Lucky Number")
else:
    print("Unlucky Number")
