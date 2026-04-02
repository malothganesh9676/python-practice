num = input()
length = len(num)

if length == 1 :
    print(int(num[0]))
elif length == 2:
    result = int(num[0]) + int(num[1])
    print(result)
elif length == 3:
    result = int(num[0]) + int(num[1]) + int(num[2])
    print(result)
elif length == 4 :
    result = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])
    print(result)
elif length == 5:
    result = int(num[0]) +  int(num[1]) + int(num[2]) + int(num[3]) + int(num[4])
    print(result)
