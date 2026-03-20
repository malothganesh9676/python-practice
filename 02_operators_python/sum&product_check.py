a = input()
b = input()

sum_of = len(a) + len(b) < 3
product = len(a) * len(b) < 3

result = sum_of and product
print(result)
