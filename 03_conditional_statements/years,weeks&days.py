n = int(input()) # 1329

years = n // 365
remaining = n % 365 

weeks = remaining // 7
remaining = remaining % 7

days = remaining

print(years)
print(weeks)
print(days)
