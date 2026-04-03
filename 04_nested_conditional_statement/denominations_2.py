amount = int(input())

no_of_500s = amount // 500 
remaining = amount % 500 

no_of_50s = remaining // 50 
remaining = remaining % 50 

no_of_10s = remaining // 10 
remaining = remaining % 10 

no_of_1s = remaining

result = ("500: " + str(no_of_500s)) + " " + ("50: " + str(no_of_50s)) + " " + ("10: " + str(no_of_10s)) + " " + ("1: " + str(no_of_1s))
print(result)
