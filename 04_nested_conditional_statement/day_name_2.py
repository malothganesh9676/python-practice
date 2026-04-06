day = input()
n = int(input())

if day == "Sunday":
    day_num = 0
elif day == "Monday":
    day_num = 1 
elif day == "Tuesday":
    day_num = 2 
elif day == "Wednesday":
    day_num = 3 
elif day == "Thursday":
    day_num = 4 
elif day == "Friday":
    day_num = 5 
elif day == "Saturday":
    day_num = 6 

target_day = (day_num + (n-1)) % 7 
    
if target_day == 0:
    print("Sunday")
elif target_day == 1:
    print("Monday")
elif target_day == 2:
    print("Tuesday")
elif target_day == 3:
    print("Wednesday")
elif target_day == 4:
    print("Thursday")
elif target_day == 5:
    print("Friday")
elif target_day == 6:
    print("Saturday")
    
