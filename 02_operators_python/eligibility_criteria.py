M = int(input())
P = int(input())
C = int(input())

is_greater = M >= 70 and P >= 60 and C >= 60
sum_of_num = M + P + C >= 180 

result = is_greater or sum_of_num
print(result)
