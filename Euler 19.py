months = [31, 28, 31, 30, 31, 30, 31, 31, 31, 31, 30, 31]

day = 1
sundays = 0

for year in range(1901, 2001):
    for month in months:
        workingMonth = month
        if month == 28 and year % 4 == 0:
            workingMonth += 1
        for d in range(1, workingMonth):
            day += 1
            if day % 7 == 0 and d == 1:
                sundays += 1
print(sundays)