
days = int(input("Enter the days: "))
hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))

daysSeconds = days * 86400
hoursSeconds = hours * 3600
minutesSeconds = minutes * 60
totalSeconds = seconds + days_Seconds + hoursSeconds + minutesSeconds

print(totalSeconds)
# ------------------------------------------------

# days = int(input("Enter the days: "))
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60
# print(seconds)

# days = int(input("Enter the days: "))
# totalSeconds = (days * 24 ) * 3600
# print(totalSeconds)