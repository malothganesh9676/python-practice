y = int(input())

a = y % 400 == 0 
b = y % 4 == 0 and y % 100 != 0

result = a or b 
if result :
    print(True)
else:
    print(False)
