n = input()
the_sum = (int(n[0]) + int(n[1])) == 7
one_of = int(n[0]) == 7 or int(n[1]) == 7 
is_div = int(n) % 7 == 0

result = the_sum or one_of or is_div
if result:
    print("Special Number")
else:
    print("Normal Number")
