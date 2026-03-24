string = input()

length = len(string)
between = length > 2 and length < 7
first_char = string[0] != "a"

result = between or first_char
if result:
    print("Valid String")
else:
    print("Not a Valid String")
