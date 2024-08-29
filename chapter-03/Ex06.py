
days = int(input("Enter the days: "))
hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))

days_seconds = days * 86400
hours_seconds = hours * 3600
minutes_seconds = minutes * 60
total_seconds = seconds + days_seconds + hours_seconds + minutes_seconds

print(total_seconds)
# ------------------------------------------------

# days = int(input("Enter the days: "))
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60
# print(seconds)

# days = int(input("Enter the days: "))
# total_seconds = (days * 24 ) * 3600
# print(total_seconds)