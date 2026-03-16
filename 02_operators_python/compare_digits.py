a = input()
b = input()

last_3_char_a = a[-3:]
last_3_char_b = b[-3:]

result = last_3_char_a == last_3_char_b
print(result)
