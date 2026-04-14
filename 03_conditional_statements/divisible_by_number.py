n = int(input()) #6
triple = n * 3 
divisible = triple % 6 == 0 

if divisible:
    print(triple)
else:
    print(n)
