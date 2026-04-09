N = int(input()) # 5

count = 1 
while count <= N:
    numbers = (str(count) + " " ) * count
    print(numbers)
    count = count + 1
