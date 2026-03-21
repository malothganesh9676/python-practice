a = int(input())
b = int(input())
c = int(input())

side_a = a+b > c 
side_b = b+c > a 
side_c = c+a > b 

result = side_a and side_b and side_c
print(result)
