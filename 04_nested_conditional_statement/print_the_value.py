string = input()
number = int(string[:-1])
last_letter = string[-1]

if last_letter == "T":
    print(number * 10)
elif last_letter == "H":
    print(number * 100)
else:
    print(number * 1000)
