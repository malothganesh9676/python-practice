amount = int(input())

no_of_100s = amount // 100 
remaining = amount % 100 

no_of_50s = remaining // 50 
remaining = remaining % 50

no_of_10s = remaining // 10 
remaining = remaining % 10 

no_of_1s = remaining // 1 
remaining = remaining % 1 

print("100:" + str(no_of_100s))
print("50:" + str(no_of_50s))
print("10:" + str(no_of_10s))
print("1:" + str(no_of_1s))
