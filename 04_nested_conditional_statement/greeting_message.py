Time = int(input())

if Time >= 4 and Time < 12:
    print("Good Morning")
elif Time >= 12 and Time < 16:
    print("Good Afternoon")
elif Time >= 16 and Time < 20:
    print("Good Evening")
else:
    print("Good Night")
