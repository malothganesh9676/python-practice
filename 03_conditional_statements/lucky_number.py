a = int(input())
b = int(input())

cond1 = a == 6 or b == 6
cond2 = a+b == 6 
cond3 = a-b == 6 or b-a == 6

result = cond1 or cond2 or cond3
if result :
    print("Lucky")
else:
    print("Not Lucky")
