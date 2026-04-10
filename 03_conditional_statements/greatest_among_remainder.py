n = int(input()) # 12

rem1 = n % 4
rem2 = n % 5

among_greatest_n = rem2 > rem1
if among_greatest_n:
    print(rem2)
else:
    print(rem1)
