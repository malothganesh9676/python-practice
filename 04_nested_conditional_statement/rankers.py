r = int(input())

is_less_than_3 = r <= 3 
is_less_than_10 = r <= 10 

if is_less_than_3:
    print("One of Top 3")
elif is_less_than_10:
    print("Not Top 3 but One of Top 10")
